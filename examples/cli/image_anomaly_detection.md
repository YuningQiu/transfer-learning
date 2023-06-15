# Image Anomaly Detection Intel® Transfer Learning Tool CLI Examples

## Transfer learning using your own dataset

The example below shows how the Intel Transfer Learning Tool CLI can be used for image anomaly detection transfer learning
using your own dataset. It performs defect analysis with the MVTec dataset using PyTorch. The workflow uses a pretrained ResNet50 v1.5 model from torchvision.

To use [MVTec](https://www.mvtec.com/company/research/datasets/mvtec-ad) or your own image dataset for anomaly detection, your image files (`.jpg` or `.png`) should be arranged in one of two ways.

Method 1: Category Folders
Arrange them in folders in the root dataset directory like this:

hazelnut
  └── crack
  └── cut
  └── good
  └── hole
  └── print
IMPORTANT: There must be a subfolder named good and at least one other folder of defective examples. It does not matter what the names of the other folders are or how many there, as long as there is at least one. This would also be an acceptable Method 1 layout:

toothbrush
  └── defective
  └── good
TLT will encode all of the non-good images as "bad" and use the "good" images in the training set and a mix of good and bad images in the validation set.

Method 2: Train & Test Folders with Category Subfolders
Arrange them in folders in the root dataset directory like this:

hazelnut
  └── train
      └── good
  └── test
      └── crack
      └── cut
      └── good
      └── hole
      └── print
When using this layout, TLT will use the exact defined split for train and validation subsets unless you use the shuffle_split method to re-shuffle and split up the "good" images with certain percentages
