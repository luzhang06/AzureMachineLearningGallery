# NLP Tasks 

This module brings the highly appraised [transformers](https://github.com/huggingface/transformers) library to Azure ML designer experiments.

You can fine-tune transformer based language models to downstream tasks using Hugging Face standard [pretrained models](https://huggingface.co/transformers/pretrained_models.html)

## Downstream tasks

The module provide support for the following downstream tasks :

- Regression
- Binary classification
- Multi-class classification

## Pretrained Models

 The supported pre-trained models for the aforementioned downstream tasks:

- ALBERT
- BERT
- CamemBERT
- DistilBERT
- ELECTRA
- FlauBERT
- RoBERTa
- XLM
- XLM-RoBERTa
- XLNet


## How to use it

- Register train and score modules
- Drag it to your experiment
- Choose among the pretrained models, choose your hyperparameters and run

![Example](https://testmlposte.blob.core.windows.net/cmcaptures/transformersPNG.PNG) 

## Notes

- Training on multi-gpu is supported. Distributed training isn't for now.
- Hugging face community pre-trained models are not supported for now.




## Acknowledgment

This module wouldn't be possible with out these great libraries:
- https://github.com/ThilinaRajapakse/simpletransformers
- https://github.com/huggingface/transformers
