# ✍🏻 Face mask detection model with YOLOV4-Tiny

![Google Colab](https://img.shields.io/badge/Editor-Google%20Colab-brightgreen)
![Python](https://img.shields.io/badge/Code-Python-blue)

<p align="center">
  <img src="https://cdn-images-1.medium.com/max/800/1*VPauyfV8aB82e7AJuQkOww.png" alt="Face mask detection model with YOLOV4-Tiny"/>
</p>

This repository contained face mask detection model by using YOLOV4-Tiny from Darknet. The model building process is required less code and it can be done by configuration. Below is the details and materials needed for develop face mask detection model by using GPU Training of Google Colab.

## Model materials
* `yolov4-tiny-custom.cfg`: 
* `obj.data`:
* `obj.names`:
* `process.py`:
* `faceMaskTiny.ipynb`:

## Setup step
1. Create Google Colab notebook and turn GPU Training on.
2. Create folder in the Google Drive to keep all files from this project. It can be named any name. In this case, the project is named `faceMaskTiny`. Changing the working directory on Colab notebook to project folder.
```
%cd /content/drive/My Drive/Colab Notebooks/faceMaskTiny
```
3. Inside the project folder, create another folder that **MUST** be named `training`. It can be created on Colab notebook using below command:
```
!mkdir training
```
4. Clone the Darknet repository into Google Drive.
```
!git clone https://github.com/AlexeyAB/darknet
```
5. Link the path name to `/mydrive`. This step is to link location path either on Google Drive or Colab space to `/mydrive`. Any space in the location path needs to insert `\` as below command:
```
!ln -s /content/drive/My\ Drive/Colab\ Notebooks/ /mydrive #Map to /mydrive
```
6. Changing the working directory on Colab notebook to **darknet** folder. Config `Makefile` to enable GPU Compiler.
```
%cd darknet/
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile
!sed -i 's/LIBSO=0/LIBSO=1/' Makefile
```
7. Compile darknet by using `!make`.
8. Clear unnecessary files inside darknet folder.
* Folder **data**: Remove all files **EXCEPT labels** folder.
* Folder **cgf**: It can be removed all files.
```
!find data/ -maxdepth 1 -type f -delete
%rm -rf cfg/
%mkdir cfg
```
9. Download 3 files from this repository:
* `obj.data`: The details of model training configuration.
```
classes = 2
train  = data/train.txt
valid  = data/test.txt
names = data/obj.names
backup = /mydrive/faceMaskTiny/training/
```
* `obj.names`: The details of labels.
```
with_mask
without_mask
```
* `yolov4-tiny-custom.cfg`: The details of YOLOV4-Tiny configuration. This file is ready to used and the changed details can be found below:
```
# Training
batch=64 #Change to 64
subdivisions=16 #Change to 16
width=416 #Change to 416
height=416 #Change to 416

...

learning_rate=0.00261
burn_in=1000
max_batches = 6000 #Change to 6000
policy=steps
steps=4800,5400 #Change to 4800 and 5400
scales=.1,.1

...

# Convolutional layer before yolo layer1
[convolutional]
size=1
stride=1
pad=1
filters=21 #Change to 21
activation=linear

[yolo]
mask = 3,4,5
anchors = 10,14,  23,27,  37,58,  81,82,  135,169,  344,319
classes=2 #Change to 2

...

# Convolutional layer before yolo layer2
[convolutional]
size=1
stride=1
pad=1
filters=21 #Change to 21
activation=linear

[yolo]
mask = 0,1,2
anchors = 10,14,  23,27,  37,58,  81,82,  135,169,  344,319
classes=2 #Change to 2
```
10. Download face mask image dataset from Kaggle
fff








## Example image result
<p align="center">
<a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/3RSryX2k/download-28.png" alt="Face mask detection model with YOLOV4-Tiny"/></a><br/><br/>
</p>

## Example image from video result

## Full video result
1. https://www.youtube.com/watch?v=nFcm4XF0fz8
2. https://www.youtube.com/watch?v=lO_xMM8i7p4
