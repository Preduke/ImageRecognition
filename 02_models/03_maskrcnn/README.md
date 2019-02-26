# Mask R-CNN

## 1. Train the model

- Login to gcloud and navigate to mrcnn:
```
cd home/unicorn/mrcnn/
```
- Copy content of train and test folder from bucket storage:
```
sudo gsutil -m cp -r gs://unicorn-analytics-bucket/upload/train/ ./samples/car/train
sudo gsutil -m cp -r gs://unicorn-analytics-bucket/upload/test/ ./samples/car/test
```

- If needed update options of config file:
```
sudo nano ./mrcnn/config.py
```

- Or set current config-file to default: 
```
sudo XXXXXXXX
```

- Start the Training and relax: 
```
sudo ./samples/car/traing.py -o simple -a ./annotations.txt
```

## 2. Test your own Data

- First copy the pictures you would like to test from bucket :
```
cd home/unicorn/mrcnn/
```
