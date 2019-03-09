# Einzelne Txt Files in der Default Ordner
# JPG Files auch in den Default Ordern, werden zum Auslesen der größe gebraucht
# Python Skript ausfuehren
# csv. in json umwandeln

import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile
from PIL import Image

download_dir ="FILE.json"
csv = open(download_dir, "w")
annotations = glob('./*.txt')
string = '{'

split1 = 0
for file in annotations:
	if split1 != 0:
		string = string + ','
	file2 = file.replace('txt', 'jpg')
	size = os.path.getsize(file2)
	pic = "./" + file2
	im=Image.open(pic)
	res = im.size
	pic_width = res[0]
	pic_height = res[1]

	filename = file.split('/')[-1].split('.')[0] + '.jpg'
	string = string + '"' + filename + str(size) + '":{"filename":"'+filename + '","size":' + str(size) + ',"regions":['
	fobj = open(file)
	split2=0
	for line in fobj:
		
		if split2 != 0:
			string = string + ','
		split2 = split2 + 1	
		word = line.split()
		#print(word)
		a_1 = int(round(float(word[1])*float(pic_width),0))
		a_2 = int(round(float(word[2])*float(pic_height),0))
		a_3 = int(round(float(word[3])*float(pic_width),0))
		a_4 = int(round(float(word[4])*float(pic_height),0))
		x_1 = a_1- (a_3)
		x_2 = a_1- (a_3)
		x_3 = a_1
		x_4 = a_1 + (a_3)
		x_5 = a_1 + (a_3)
		x_6 = a_1 + (a_3)
		x_7 = a_1
		x_8 = a_1- (a_3)
		
		y_1 = a_2
		y_2 = a_2 -(a_4)
		y_3 = a_2 -(a_4)
		y_4 = a_2 -(a_4)
		y_5 = a_2 
		y_6 = a_2  + a_4
		y_7 = a_2  + a_4
		y_8 = a_2  + a_4
		string = string + '{"shape_attributes":{"name":"polygon","all_points_x":[' + str(x_1) + ',' + str(x_2) + ',' + str(x_3) + ',' + str(x_4) + ',' + str(x_5) + ',' + str(x_6) + ',' + str(x_7) + ',' + str(x_8) + '],"all_points_y":[' + str(y_1) + ',' + str(y_2) + ',' + str(y_3) + ',' + str(y_4) + ',' + str(y_5) + ',' + str(y_6) + ',' + str(y_7) + ',' + str(y_8) + ']},"region_attributes":{}}'	
	string = string + '],"file_attributes":{}}'
	split1 = split1 + 1


string = string + '}'
csv.write(string)

