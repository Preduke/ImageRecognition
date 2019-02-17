# Einzelne Txt Files in der Default Ordner
# JPG Files auch in den Default Ordern, werden zum Auslesen der größe gebraucht
# Python Skript ausfuehren

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
		x_min = word[0]
		x_max = word[2]
		y_min = word[1]
		y_max = word[3]
		width = int(word[2]) - int(word[0])
		height = int(word[3]) - int(word[1])
		string = string + '{"shape_attributes":{"name":"rect","x":' + str(x_min) + ',"y":' + str(y_min) + ',"width":' + str(width) + ',"height":'+ str(height) +'},"region_attributes":{}}'	
	string = string + '],"file_attributes":{}}'
	split1 = split1 + 1

string = string + '}'

csv.write(string)

