# Einzelne Txt Files in der Default Ordner
# JPG Files auch in den Default Ordern, werden zum Auslesen der größe gebraucht
# Python Skript ausfuehren
# csv. in json umwandeln

import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile

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
	filename = file.split('/')[-1].split('.')[0] + '.jpg'
	string = string + '"' + filename + str(size) + '":{"filename":"'+filename + '","size":' + str(size) + ',"regions":['
	fobj = open(file)
	split2=0
	for line in fobj:
		
		if split2 != 0:
			string = string + ','
		split2 = split2 + 1	
		word = line.split()
		x_1 = word[0]
		x_2 = word[2]
		x_3 = word[2]
		x_4 = word[0]
		x_5 = int((float(x_1) + float(x_2))/2)
		x_6 = int((float(x_1) + float(x_3))/2)
		x_7 = word[0]
		x_8 = word[2]
		y_1 = word[1]
		y_2 = word[1]
		y_3 = word[3]
		y_4 = word[3]
		y_5 = word[1]
		y_6 = word[3]
		y_7 = int((float(y_1) + float(y_3))/2)
		y_8 = int((float(y_1) + float(y_3))/2)
		string = string + '{"shape_attributes":{"name":"polygon","all_points_x":[' + str(x_1) + ',' + str(x_2) + ',' + str(x_3) + str(x_4) + ',' + str(x_5) + ',' + str(x_6) + ',' + str(x_7) + ',' + str(x_8) + ',' + '],"all_points_y":[' + str(y_1) + ',' + str(y_2) + ',' + str(y_3) + str(y_4) + ',' + str(y_5) + ',' + str(y_6) + ',' + str(y_7) + ',' + str(y_8) + ',' +']},"region_attributes":{}}'	
	string = string + '],"file_attributes":{}}'
	split1 = split1 + 1


string = string + '}'
csv.write(string)

