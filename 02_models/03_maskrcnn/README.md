# Mask R-CNN

## 1. Train the model

Login to gcloud and navigate to mrcnn:
```
cd home/unicorn/mrcnn/
```
Remove old Files & Copy content of train and test folder from bucket storage:
```
sudo rm -r ./samples/car/train/*
sudo rm -r ./samples/car/test/* 
sudo gsutil -m cp -r gs://unicorn-analytics-bucket/upload/train/ ./samples/car/train
sudo gsutil -m cp -r gs://unicorn-analytics-bucket/upload/test/ ./samples/car/test
```

If needed update options of config file:
```
sudo nano ./mrcnn/config.py
```

Or set current config-file to default: 
```
sudo XXXXXXXX
```
Start the Training and relax on your bike :mountain_bicyclist:: 
```
sudo ./samples/car/traing.py -o simple -a ./annotations.txt
```
Get your weight-file that has been generated: 
```
sudo XXXXXXXXX
```
From time-to-time delete weight files: 
```
sudo XXXXXXXXX
```

## 2. Test your own Data

Navigate to Test Folder :
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
sudo rm -r ./result/*
```
Start recognition :
```
cd XXXXXXXXXXXXXX
```
Generated pictures will be saved in /result folder

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
