# -*- coding: utf-8 -*-

import os
from os import walk, getcwd
from PIL import Image

classes = ["1","002","003","004","005","006"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""
## Ordnerstruktur:
#git: 
#convert.py
#Ordner "anno" (Hier sind die ursprünglichen annotations drin)
#Ordner "output"
#Falls die Ordner anders heißen bei euch, die zwei Zeilen untendrunter anpassen
mypath = "./anno/"
outpath = "./output/"

cls = "1"
if cls not in classes:
    exit(0)
cls_id = classes.index(cls)

wd = getcwd()
list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
print(txt_name_list)

""" Process """
for txt_name in txt_name_list:
    
    """ Open input text files """
    txt_path = mypath + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
    
    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "a")
    
    
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        #print('lenth of line is: ')
        print(len(line))
        #print('\n')
        elems = line.split(' ')
        if(len(elems) >= 2):
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            cat = elems[4]
            print(elems)
            shit = str(cat + " " + elems[0] + " " + elems[1] + " " + elems[2] + " " + elems[3])
            txt_outfile.write(str(shit) + '\n')
                
list_file.close()  