# Spectral Residual Anomaly Detection 

## Overview

This sample pipeline contains some components that implement with spectral residual anomaly detection. This algorithm can be used in Time Series anomaly detection.

This pipeline build a time-series anomaly detection model which can help customers monitor time-series and detect incidents.

#### You will learn how to:

Build pipeline with newly created components and a manufacture sample dataset.

## Prerequisites

[Create related components in your workspace](.../tutorial/tutorial1-use-existing-components.md).

## Build the pipeline

1. Register this [AnomalyDetector-Manufacture dataset](https://github.com/microsoft/Cognitive-Samples-IntelligentKiosk/blob/master/Kiosk/Assets/AnomalyDetector/AnomalyDetector-Manufacture.csv) as File dataset in your workspace.

You can also use your own dataset, make sure that it is registered as File dataset with following format, and the count of time series must be more than 12:

|Timestamp|Value|
|---|---|
|2018/7/1 0:00|22|
|2018/7/1 2:00|22|
|2018/7/1 4:00|22|
|2018/7/1 6:00|22|
|2018/7/1 8:00|52.93218322|
|2018/7/1 10:00|52.81943684|
|2018/7/1 12:00|52.33277765|
|2018/7/1 14:00|52.82106858|
|2018/7/1 16:00|52.93218322|
|2018/7/1 18:00|22|
|2018/7/1 20:00|22|
|2018/7/1 22:00|22|
|2018/7/2 0:00|22|
|2018/7/2 2:00|22|
|2018/7/2 4:00|22|
|2018/7/2 6:00|22|

1. Add **Spectral Residual Anomaly Detection** to canvas, connect it to the dataset, and configure the parameters.

1. Submit the pipeline.

## Related components
| Component spec               | Description                                                  |
| --- |--- |
[Spectral Residual Anomaly Detection](https://github.com/microsoft/anomalydetector/blob/master/aml_module/module_spec.yaml)| Detect anomlies based on spectral residual anomaly detection algorithm. |


| Contributed by | Maintained by | Category | Tags | Last update | 
|---|---|---|---|---|
| Microsoft | @Microsoft Open Source | Tutorials |recommendation| September 4, 2020 |

<a href="https://trackgit.com">
<img src="https://sfy.cx/u/oFu" alt="trackgit-views" />
</a> views