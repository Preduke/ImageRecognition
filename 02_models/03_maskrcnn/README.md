# Mask R-CNN

## 1. Train the model

Login to gcloud and navigate to mrcnn:
```
cd /home/unicorn/mrcnn/
```
Remove old Files & Copy content of train and test folder from bucket storage.
Please make sure that annotation json file is also available in each of the folder. 
```
sudo rm -r ./samples/car/train/*
sudo rm -r ./samples/car/test/* 
sudo gsutil -m cp gs://unicorn-analytics-bucket/zusammen/train/* ./samples/car/train/
sudo gsutil -m cp gs://unicorn-analytics-bucket/zusammen/test/* ./samples/car/train/
```

If needed update options of config file:
```
sudo nano ./mrcnn/config.py
```

Or set current config-file to default: 
```
sudo XXXXXXXX
```
Navigate to folder, start the Training and relax on your bike :mountain_bicyclist:: 
```
cd samples/car/
sudo python3 ./car.py train --dataset=./ --weights=./mask_rcnn_coco.h5
```
Get your weight-file that has been generated: 
```
cd /home/unicorn/mrcnn/
sudo cp /logs/[ADJUST FOLDER]/mask_rcnn_car_0030.h5 ./
```
From time-to-time delete weight files: 
```
sudo rm -r ./logs/* 
```

## 2. Test your own Data

Navigate to Test Folder :
```
cd home/unicorn/mrcnn/
```
First copy the pictures you would like to test from bucket :
```
sudo rm -r ./images/*
sudo gsutil -m cp gs://unicorn-analytics-bucket/zusammen/eval/* ./images/
```
Copy the trained weights you would like to use :
```
sudo rm mask_rcnn_car_0030.h5
sudo cp logs/[ADJUST FOLDER]/mask_rcnn_car_0030.h5 ./
```
Clean the result folder:
```
sudo rm -r ./results/*
```
Start recognition :
```
sudo python3 TESTMODEL.py
```
Generated pictures will be saved in /results folder

## 3. Test your data and extract annotations

Navigate to Test and Extract Folder :
```
cd home/unicorn/mrcnn/
```
First copy the pictures you would like to test from bucket :
```
cd home/unicorn/mrcnn/
```
Copy the trained weights you would like to use :
```
cd XXXXXXXXXXXXXX
```
Clean the result folder:
```
cd XXXXXXXXXXXXXX
```
Start recognition :
```
cd XXXXXXXXXXXXXX
```
