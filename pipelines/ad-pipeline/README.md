# Spectral Residual Anomaly Detection 

## Overview

This sample pipeline contains some components that implement with spectral residual anomaly detection scenarios.

This pipeline build a time-series anomaly detection model which can help customers monitor time-series and detect incidents.

#### You will learn how to:

Build pipeline with newly created components and a manufacture sample dataset.

## Prerequisites

[Create related components in your workspace](.../tutorial/tutorial1-use-existing-components.md).

## Build the pipeline

1. Register this [AnomalyDetector-Manufacture dataset](https://github.com/microsoft/Cognitive-Samples-IntelligentKiosk/blob/master/Kiosk/Assets/AnomalyDetector/AnomalyDetector-Manufacture.csv) as File dataset in your workspace.

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