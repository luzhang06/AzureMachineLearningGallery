Convert Labeling Data to Image Directory Component
=========================================
This component is to convert "Data Labeling" export dataset to 'Designer' image directory.

Dataset
-----------------------------
Exported dataset as Azure ML Dataset in "Data Labeling" project. Type 'Image Classification Multi-class' and 'Image Classification Multi-label' are supported in this component.

Sample pipeline graph
-----------------------------
In this example, we use this component to replace "Convert to Image Directory" component in sample "Image Classification using DenseNet".
![Pipeline graph](./pipeline.png)
