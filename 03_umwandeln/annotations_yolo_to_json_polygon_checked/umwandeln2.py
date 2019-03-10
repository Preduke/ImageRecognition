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
		if (a_1- (a_3)) >= pic_width:
			x_1 = pic_width - 2
		else:
			if (a_1- (a_3)) <= 0:
				x_1 = 1
			else: 
				x_1 = a_1- (a_3)

		if (a_1- (a_3)) >= pic_width:
			x_2 = pic_width - 2
		else:
			if (a_1- (a_3)) <= 0:
				x_2 = 1
			else: 
				x_2 = a_1- (a_3)

		
		if (a_1) >= pic_width:
			x_3 = pic_width - 2
		else:
			x_3 = a_1

		if (a_1 + (a_3)) >= pic_width:
			x_4 = pic_width - 2
		else:
			x_4 = a_1 + (a_3)

		if (a_1 + (a_3)) >= pic_width:
			x_5 = pic_width - 2
		else:
			x_5 = a_1 + (a_3)

		if (a_1 + (a_3)) >= pic_width:
			x_6 = pic_width - 2
		else:
			x_6 = a_1 + (a_3)

		if (a_1) >= pic_width:
			x_7 = pic_width - 2
		else:
			x_7 = a_1

		if (a_1- (a_3)) >= pic_width:
			x_8 = pic_width - 2
		else:
			if (a_1- (a_3)) <= 0:
				x_8 = 1
			else: 
				x_8 = a_1- (a_3)


		if (a_2) >= pic_height:
			y_1 = pic_height - 2
		else:
			y_1 = a_2

		if (a_2 -(a_4)) >= pic_height:
			y_2 = pic_height - 2
		else:
			if (a_2 -(a_4)) <= 0:
				y_2 = 1
			else: 
				y_2 = a_2 -(a_4)
		
		if (a_2 -(a_4)) >= pic_height:
			y_3 = pic_height - 2
		else:
			if (a_2 -(a_4)) <= 0:
				y_3 = 1
			else: 
				y_3 = a_2 -(a_4)

		if (a_2 -(a_4)) >= pic_height:
			y_4 = pic_height - 2
		else:
			if (a_2 -(a_4)) <= 0:
				y_4 = 1
			else: 
				y_4 = a_2 -(a_4)

		if (a_2 ) >= pic_height:
			y_5 = pic_height - 2
		else:
			y_5 = a_2 

		if (a_2  + a_4) >= pic_height:
			y_6 = pic_height - 2
		else:
			y_6 = a_2  + a_4

		if (a_2  + a_4) >= pic_height:
			y_7 = pic_height - 2
		else:
			y_7 = a_2  + a_4

		if (a_2  + a_4) >= pic_height:
			y_8 = pic_height - 2
		else:
			y_8 = a_2  + a_4

		string = string + '{"shape_attributes":{"name":"polygon","all_points_x":[' + str(x_1) + ',' + str(x_2) + ',' + str(x_3) + ',' + str(x_4) + ',' + str(x_5) + ',' + str(x_6) + ',' + str(x_7) + ',' + str(x_8) + '],"all_points_y":[' + str(y_1) + ',' + str(y_2) + ',' + str(y_3) + ',' + str(y_4) + ',' + str(y_5) + ',' + str(y_6) + ',' + str(y_7) + ',' + str(y_8) + ']},"region_attributes":{}}'	
	string = string + '],"file_attributes":{}}'
	split1 = split1 + 1


string = string + '}'
csv.write(string)

