# Spectral Residual Anomaly Detection

**Spectral Residual Anomaly Detection** component is based on open source spectral residual anomaly detection algorithm, developed by Microsoft. 

The details of the Spectral Residual algorithm can be found at https://arxiv.org/pdf/1906.03821.pdf.

## Component spec

[Here](https://github.com/microsoft/anomalydetector/blob/master/aml_module/module_spec.yaml) is the component spec. You can use it to create a new component in you Azure Machine Learning workspace.

## Create new component in your workspace

In the Azure Machine Learning studio portal, you can create new component in your workspace and use it in the designer.
1. Go to **Modules** asset page.
1. Click on **New Module** and select **From Yaml file**.
1. Input the component spec URL and Click **Next**
1. Follow the guidance to finish your creation. And You could find your new components under **Custom Module** in the module list of Designer.