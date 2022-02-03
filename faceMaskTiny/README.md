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
9. Download 4 files from this repository:
* `process.py`: The python script to generate training and validation files.
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
10. Download face mask image dataset, which already labelled from Kaggle by link below:
* https://www.kaggle.com/techzizou/labeled-mask-dataset-yolo-darknet
11. Upload all files and dataset to Google Drive into project folder NOT IN **darknet**.

This step is optional. It can be done manually or by using command.

12. The current is **darknet** folder. First, copy dataset in `.zip` format into `/darknet/` folder and unzip it into `/darknet/data/`.
```
!cp /mydrive/faceMaskTiny/obj.zip ../
!unzip ../obj.zip -d data/
```
13. Copy `yolov4-tiny-custom.cfg` into `/darknet/cfg/`.
```
!cp /mydrive/faceMaskTiny/yolov4-tiny-custom.cfg ./cfg/
```
14. Copy `obj.names` and `obj.data` into `/darknet/data/`.
```
!cp /mydrive/faceMaskTiny/obj.names ./data/
!cp /mydrive/faceMaskTiny/obj.data  ./data/
```
15. Copy processs script `process.py` into the `/darknet/`.
```
!cp /mydrive/faceMaskTiny/process.py ./
```
16. Run python script. It can be used `2>/dev/null` to hide the log process.
```
!python process.py 2>/dev/null
```
17. The python script will create 2 files, which are `test.txt` and `train.txt` into `/darknet/data/`.
18. Download the pre-trained **YOLOv4-tiny weights**.
```
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29
```
19. Begin the training process. The model will train for 6000 iterations based on the configuration. Usually, it takes up 2 hours to finish. However, it can be early stopped if the model loss does not have the improvement, around **30%** is recommended.
```
!./darknet detector train data/obj.data cfg/yolov4-tiny-custom.cfg yolov4-tiny.conv.29 -dont_show -map 2>/dev/null
```

<p align="center">
  <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/wMfHDYNp/download-29.png" alt="Face mask detection model with YOLOV4-Tiny"/></a><br/><br/>
</p>

20. If the training process was stopped or crashed, it would restart by following command:
```
!./darknet detector train data/obj.data cfg/yolov4-tiny-custom.cfg /mydrive/faceMaskTiny/training/yolov4-tiny-custom_last.weights -dont_show -map 2>/dev/null
```

## Example image result
After finishing the training process, the configuration `yolov4-tiny-custom.cfg` has to be changed prior using the model. Changing `batch=64` to `batch=1` and `subdivisions=16` to `subdivisions=1`.
```
%cd cfg
!sed -i 's/batch=64/batch=1/' yolov4-tiny-custom.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov4-tiny-custom.cfg
%cd ..
```
An example image for testing model:

<p align="center">
  <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/CxZDBF8w/mask2.jpg" alt="Face mask detection model with YOLOV4-Tiny"/></a><br/><br/>
</p>

To test with image, it can be used following command:
```
!./darknet detector test data/obj.data cfg/yolov4-tiny-custom.cfg /mydrive/faceMaskTiny/training/yolov4-tiny-custom_best.weights /mydrive/faceMaskTiny/testFiles/mask2.jpg -thresh 0.3 2>/dev/null
```

<p align="center">
  <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/3RSryX2k/download-28.png" alt="Face mask detection model with YOLOV4-Tiny"/></a><br/><br/>
</p>

## Example image from video result
To test with video, it can be used following command:
```
!./darknet detector demo data/obj.data cfg/yolov4-tiny-custom.cfg /mydrive/faceMaskTiny/training/yolov4-tiny-custom_best.weights -dont_show /mydrive/faceMaskTiny/testFiles/videoTest1.mp4 -thresh 0.7 -i 0 -out_filename /mydrive/faceMaskTiny/videoResult1.avi
```

The snapshots result from the video:
<p align="center">
  <a href="https://postimages.org/" target="_blank"><img src="https://i.postimg.cc/3RSryX2k/download-28.png" alt="Face mask detection model with YOLOV4-Tiny"/></a><br/><br/>
</p>


## Full video result
1. https://www.youtube.com/watch?v=nFcm4XF0fz8
2. https://www.youtube.com/watch?v=lO_xMM8i7p4
