# Image Anomaly Detection Intel® Transfer Learning Tool CLI Examples

## Transfer learning using your own dataset

The example below shows how the Intel Transfer Learning Tool CLI can be used for image anomaly detection transfer learning
using your own dataset. It performs defect analysis with the MVTec dataset using PyTorch. The workflow uses a pretrained ResNet50 v1.5 model from torchvision.


## Transfer learning using a dataset from catalog

This example shows the Intel Transfer Learning Tool CLI being used for image anomaly detection transfer learning
using the [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad) dataset.

### Download dataset
+ Download MVTec Anomaly Detection Dataset
Follow instructions at [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad) to obtain the example dataset.

### Transfer learning
```bash
# Create dataset and output directories
DATASET_DIR=/tmp/data
OUTPUT_DIR=/tmp/output
mkdir -p ${DATASET_DIR}
mkdir -p ${OUTPUT_DIR}

# Name of the dataset to use
DATASET_NAME=hazelnut

# Train resnet_v1_50 using the MVTec dataset ResNet50 v1.5 model from torchvision
tlt train \
    -f pytorch \
    --model-name resnet50 \
    --dataset-name ${DATASET_NAME} \
    --dataset-dir ${DATASET_DIR} \
    --output-dir ${OUTPUT_DIR} \
    --epochs 2

# Evaluate the model exported after training
# Note that your --model-dir path may vary, since each training run creates a new directory
tlt eval \
    --model-dir ${OUTPUT_DIR}/resnet50/1 \
    --dataset-name ${DATASET_NAME} \
    --dataset-dir ${DATASET_DIR}
```

## Citations

```
@ONLINE {MVTec,
author = "MVTec Software GmbH",
title = "Hazelnut",
month = "jun",
year = "2019",
url = "https://www.mvtec.com/company/research/datasets/mvtec-ad"}
```
