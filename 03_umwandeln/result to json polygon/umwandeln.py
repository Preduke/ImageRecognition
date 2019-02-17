# Hiermit wandeln wir die Ergebnisse der Objekterkennung von masrk rcnn in eine polygon json 
# Annotation Files um. Diese kann dann in via importiert werden und man kann die Annotations ggf. anpassen. 
# 
# 1. Files aus der mask rcnn Detection in den Ordner kopieren
# 2. umwandeln.py ausführen
# 3. Die generierte OUTPUT.csv in .json umbenennen

import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile
import re


annotations = glob('./*.csv')
string = '{'

# Als erstes muessen wir einen Faktor finden, der den Abstand der Punkte des Polygon automatisch 
# bestimmt. Das kann je nach Größe der Objekte sehr unterschiedlich sein. 
# Wenn der Abstand zu groß bzw. klein ist kann er hier auch angepasst werden. 
# Einfach zum Faktor k am Ende Pixel hinzufügen oder abziehen. 
for file in annotations:
	x = []
	y = []
	fobj = open(file)
	counter=0
	for line in fobj:
		# Wir entfernen das erste "
		if counter == 0:
			line = line[1:]
		# Wenn das nächste Objekt kommt beenden wir die List Befüllung
		if line[0] == '"':
			break

		x1 =  line.replace(".5", "")
		x1 = re.findall('\d+', x1 )
		
		if x1[0] and x1[1]:
			x.append(int(x1[0]))
			y.append(int(x1[1]))

		counter = counter +1
		
	xmax = max(x)
	xmin = min(x)
	ymax = max(y)
	ymin = min(y)
	k = (((xmax-xmin)*2)+((ymax-ymin)*2))/20		


for file in annotations:

	x = []
	y = []

	file2 = file.replace('csv', 'jpg')
	size = os.path.getsize(file2)
	filename = file.split('/')[-1].split('.')[0] + '.jpg'
	string = string + '"' + filename + str(size) + '":{"filename":"'+filename + '","size":' + str(size) + ',"regions":['
	fobj = open(file)

	counter=0
	for line in fobj:
		if counter == 0:
			line = line[1:]
		
		if line[0] == '"':
			string = string + '{"shape_attributes":{"name":"polygon","all_points_x":' + str(x) + ',"all_points_y":' + str(y) +'},"region_attributes":{}},'
			x = []
			y = []
		
		
		x1 =  line.replace(".5", "")

		x1 = re.findall('\d+', x1 )

		if x1[0] and x1[1]:
			# Wenn counter 0 werden die Koordinaten einfach genommen
			if counter == 0:
				x.append(int(x1[0]))
				y.append(int(x1[1]))					
				x_old = int(x1[0])
				y_old = int(x1[1])
			# Wenn counter >0 dann werden erst die alten Werte mit den neuen verglichen
			# Nur wenn der Abstand größer k ist werden die Koordinaten gespeichert
			if counter > 0:
				if (abs(int(x1[0]) - x_old) > k) or (abs(int(x1[1])) - y_old > k):
					x.append(int(x1[0]))
					y.append(int(x1[1]))
					x_old = int(x1[0])
					y_old = int(x1[1])


		counter = counter +1
		
	string = string[:-1]	
	string = string + '],"file_attributes":{}},'

	#print(string)
# Das letzte Komma entfernen und den json String beenden
string = string[:-1]	
string = string + '}'
download_dir ="OUTPUT.csv"
csv = open(download_dir, "w")
csv.write(string)

