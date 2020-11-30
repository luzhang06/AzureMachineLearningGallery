import fire
from pathlib import Path
from tempfile import mkdtemp

from azureml.contrib.dataset import FileHandlingOption
from azureml.core import Dataset
from azureml.core import Run
from azureml.data import FileDataset
from azureml.studio.core.io.image_directory import ImageDirectory
from azureml.studio.core.io.image_schema import ImageSchema
from azureml.studio.core.utils.jsonutils import (dump_to_json_file, dump_to_json_lines)
from azureml.designer.modules.computer_vision.preprocess.convert_to_image_directory.convert_to_image_directory import \
    convert as convert_file_dataset

_IMAGE_FILE_PATH = 'image'
_META_FILE_PATH = '_meta.yaml'
# supported labeling project dataset types.
LABELING_DATA_LABEL_TYPES = {'MultiLabelClassification', 'Classification'}


def get_label(row):
    # follow format of labeling project dataset.
    label = row['label']
    if isinstance(label, str):
        return label
    elif isinstance(label, list):
        label_conf = row['label_confidence']
        label, _ = sorted(zip(label, label_conf), key=lambda x: x[1], reverse=True)[0]
        return label
    else:
        raise NotImplementedError(f"Label column type '{type(label)}' is unsupported.")


def generate_image_list_schema(df, labeling_data_type, image_file_path):
    image_list = []
    categories = set()
    schema = None
    if labeling_data_type in LABELING_DATA_LABEL_TYPES:
        for index, row in df.iterrows():
            label = get_label(row)
            categories.add(label)
            image_list.append({
                ImageSchema.DEFAULT_IMAGE_REF_COL: {
                    'file_name': f"{_IMAGE_FILE_PATH}/{Path(row['image_url']).relative_to(image_file_path.resolve())}",
                },
                ImageSchema.DEFAULT_CLASSIFICATION_COL: label,
                ImageSchema.DEFAULT_ID_COL: index,
            })
        categories = sorted(list(categories))
        schema = ImageSchema.get_default_classification_schema([{
            'id': i,
            'name': category
        } for i, category in enumerate(categories)])
    else:
        raise NotImplementedError(f"Dataset label type '{labeling_data_type}' is not supported now.")

    return image_list, schema


def dump(image_list, schema, output_image_dir):
    meta = ImageDirectory.create_meta()
    if image_list:
        dump_to_json_lines(image_list, output_image_dir / ImageDirectory.IMAGE_LIST_FILE)

    if schema:
        dump_to_json_file(schema.to_dict(), output_image_dir / ImageDirectory._SCHEMA_FILE_PATH)
        meta.update_field('schema', ImageDirectory._SCHEMA_FILE_PATH, override=True)

    dump_to_json_file(meta.to_dict(), output_image_dir / _META_FILE_PATH)
    if image_list and schema:
        # generate samples
        image_dir = ImageDirectory.load(output_image_dir)
        samples = image_dir.get_samples()
        dump_to_json_file(samples, output_image_dir / ImageDirectory._SAMPLES_FILE_PATH)
        # update meta
        image_dir.meta.update_field('samples', ImageDirectory._SAMPLES_FILE_PATH, override=True)
        dump_to_json_file(image_dir.meta.to_dict(), output_image_dir / _META_FILE_PATH)


def parse_id_to_dataset(dataset_id):
    run = Run.get_context()
    ws = run.experiment.workspace
    return Dataset.get_by_id(ws, id=dataset_id)


def convert(dataset_id, output_image_dir):
    dataset = parse_id_to_dataset(dataset_id=dataset_id)
    # support file dataset as input so this module can be used in batch inference.
    if isinstance(dataset, FileDataset):
        target_path = mkdtemp()
        dataset.download(target_path=target_path, overwrite=True)
        convert_file_dataset(target_path, output_image_dir)
        return

    try:
        output_image_dir = Path(output_image_dir)
        image_file_path = output_image_dir / _IMAGE_FILE_PATH
        # labeling_data must come from 'data labeling' project output dataset.
        labeling_data = dataset
        df = labeling_data.to_pandas_dataframe(file_handling_option=FileHandlingOption.DOWNLOAD,
                                               target_path=str(image_file_path),
                                               overwrite_download=True)
        labeling_data_type = labeling_data.label['type']
        # generate image_list, schema.
        image_list, schema = generate_image_list_schema(df=df,
                                                        labeling_data_type=labeling_data_type,
                                                        image_file_path=image_file_path)
        # dump image_list, schema, meta and samples.
        dump(image_list, schema, output_image_dir)
    except Exception as e:
        raise NotImplementedError(f"Failed to convert labeling data due to '{e}'.")


if __name__ == '__main__':
    fire.Fire(convert)
