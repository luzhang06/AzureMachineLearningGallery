# Detect languages module
<br>

The Detect Languages module purpose is to analyze text input and identify the language associated with each record in the input in Azure Machine Learning studio designer experiment.

The language detection module can identify up to 170 languages uing Fasttext. The module will also output the likelihood of the predicted language.

## How to use it

Straight forward to use, simply connect your dataset to the module and provide your text column or comma seperated list if you want run detection on more than one column.
<br>

![setup](https://testmlposte.blob.core.windows.net/cmcaptures/dl1.PNG) 

One executed, the output dataset will contains the language detected with the highest likelihood for each requested column 
<br>

![output](https://testmlposte.blob.core.windows.net/cmcaptures/dl2.PNG)


## Citation
- https://github.com/facebookresearch/fastText/
```
@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}