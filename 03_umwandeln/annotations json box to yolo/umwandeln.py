# json Polygon File aus VIA in den Default Ordner
# Alle Bilder (die auch in der JSON sind) in den pics Ordner, dort wird die Auflösung der Bilder ausgelesen
# Python Skript ausfuehren


# sudo apt-get install python-pil
import json
import os
from PIL import Image
from pprint import pprint
import pandas as pd

# json File im gleichen Ordner
with open('via_region_data.json') as f:
	data = json.load(f)

# Folder fuer die Bilder, die werden gebracuht um die Filesize auszulesen
#PIC_DIR = os.path.abspath("/home/admin-ubuntu/analytics/umwandeln/annotations json polygon to yolo/pics/")
PIC_DIR = os.path.abspath("./pics/")
for (k,v) in data.items():
	df = []
	name = k
	filename = v['filename']
	# Achtung, wenn Fileendung nicht jpg dann hier anpassen:
	filename_2 = filename.replace('.jpg', '.txt')

	pic = PIC_DIR + "/" + filename
	im=Image.open(pic)
	res = im.size
	pic_width = res[0]
	pic_height = res[1]

	size = v['size']
	regions = v['regions']
	x_values = v['regions']
	for i in x_values:
		dict1 = i['shape_attributes']	
		for p in dict1:
			print(dict1)
			x_point = float((dict1['x']))
			y_point = float((dict1['y']))
			width = float((dict1['width']))
			height = float((dict1['height']))
			df_class = '0'
			df_x = float(x_point) / float(pic_width)
			df_y = float(y_point) / float(pic_height)
			df_weight = float(width) / float(pic_width)
			df_height = float(height) / float(pic_height)
		row = [str(df_class), str(df_x), str(df_y), str(df_weight), str(df_height)]
		df.append(row)
	
	data = pd.DataFrame(df, columns=['df_class', 'df_x', 'df_y', 'df_weight', 'df_height'])
	# Datframe speichern, 
	data[['df_class', 'df_x', 'df_y', 'df_weight', 'df_height']].to_csv(filename_2,header=False,sep=' ', index=False)
