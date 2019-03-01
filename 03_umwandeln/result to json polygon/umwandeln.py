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
	p = []
	q = []
	fobj = open(file)
	if os.stat(file).st_size == 0:
		continue

	counter=0
	for line in fobj:
		# Wir entfernen das erste ^
		if counter == 0:
			line = line[1:]
		# Wenn das nächste Objekt kommt beenden wir die List Befüllung
		if line[0] == '^':
			break
		
		x2 =  line.replace(".5", "")
		x2 = re.findall('\d+', x2 )

		for firstItem in x2:
        		o1 = firstItem
		for lastItem in x2:
			o2 = lastItem

		if 'o1' in locals():
			if o1 and o2:
				p.append(int(o1))
				q.append(int(o2))
		
		counter = counter +1
	
	xmax = max(p)
	xmin = min(p)
	ymax = max(q)
	ymin = min(q)
	k = (((xmax-xmin)*2)+((ymax-ymin)*2))/20
	k = 5			



for file in annotations:
	
	x = []
	y = []

	file2 = file.replace('csv', 'jpg')
	size = os.path.getsize(file2)
	filename = file.split('/')[-1].split('.')[0] + '.jpg'
	if os.stat(file).st_size == 0:
		continue
	string = string + '"' + filename + str(size) + '":{"filename":"'+filename + '","size":' + str(size) + ',"regions":['
	fobj = open(file)

	counter=0
	for line in fobj:
		if counter == 0:
			line = line[1:]
			#line = line +1
		
		if line[0] == '^':
			#line = line +1
			string = string + '{"shape_attributes":{"name":"polygon","all_points_x":' + str(x) + ',"all_points_y":' + str(y) +'},"region_attributes":{}},'
			x = []
			y = []
		
		
		x1 =  line.replace(".5", "")

		x1 = re.findall('\d+', x1 )
		#print(x1)
		#print(x1[0:1:])
		#print(x1[-1:])
		#numbers = [ int(x) for x in x1 ]
		for firstItem in x1:
        		z1 = x1[0:1:]
        		z1 = int(''.join(str(i) for i in z1))
        		#print(z1)
			
		for lastItem in x1:
			z2 = x1[-1:]
			z2 = int(''.join(str(i) for i in z2))
			#print(z2)

		if 'z1' in locals():
			if z1 and z2:
				# Wenn counter 0 werden die Koordinaten einfach genommen
				if counter == 0:
					x.append(int(z1))
					y.append(int(z2))					
					x_old = int(z1)
					y_old = int(z2)
				# Wenn counter >0 dann werden erst die alten Werte mit den neuen verglichen
				# Nur wenn der Abstand größer k ist werden die Koordinaten gespeichert
				if counter > 0:
					if (abs(int(z1) - x_old) > k) or (abs(int(z2)) - y_old > k):
						x.append(int(z1))
						y.append(int(z2))
						x_old = int(z1)
						y_old = int(z2)

		if 'z1' in locals():
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

