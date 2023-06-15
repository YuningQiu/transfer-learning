# Image Anomaly Detection Intel® Transfer Learning Tool CLI Examples

## Transfer learning using your own dataset

The example below shows how the Intel Transfer Learning Tool CLI can be used for image anomaly detection transfer learning
using your own dataset. It performs defect analysis with the MVTec dataset using PyTorch. The workflow uses a pretrained ResNet50 v1.5 model from torchvision.

```bash
# Create dataset and output directories
DATASET_DIR=/tmp/data
OUTPUT_DIR=/tmp/output
mkdir -p ${DATASET_DIR}
mkdir -p ${OUTPUT_DIR}



## Transfer learning using a dataset from the TFDS catalog

This example shows the Intel Transfer Learning Tool CLI being used for image classification transfer learning
using the `tf_flowers` dataset from the
[TensorFlow Datasets (TFDS) catalog](https://www.tensorflow.org/datasets/catalog/overview).

```bash
# Create dataset and output directories
DATASET_DIR=/tmp/data
OUTPUT_DIR=/tmp/output
mkdir -p ${DATASET_DIR}
mkdir -p ${OUTPUT_DIR}

# Name of the dataset to use
DATASET_NAME=hazelnut

# Train resnet_v1_50 using the TFDS catalog dataset ResNet50 v1.5 model from torchvision
tlt train \
    -f tensorflow \
    --model-name resnet_v1_50 \
    --dataset-name ${DATASET_NAME} \
    --dataset-dir ${DATASET_DIR} \
    --output-dir ${OUTPUT_DIR} \
    --epochs 2

# Evaluate the model exported after training
# Note that your --model-dir path may vary, since each training run creates a new directory
tlt eval \
    --model-dir ${OUTPUT_DIR}/resnet_v1_50/1 \
    --dataset-name ${DATASET_NAME} \
    --dataset-dir ${DATASET_DIR}
```

## Citations

```
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }
```
