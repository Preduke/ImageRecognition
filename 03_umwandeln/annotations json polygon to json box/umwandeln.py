# json Poylon File aus VIA in den Default Ordner
# Python Skript ausfuehren


import json
from pprint import pprint

download_dir ="FILE.json"
csv = open(download_dir, "w")

with open('via_region_data.json') as f:
	data = json.load(f)

string = '{'
count = 0
for (k,v) in data.items():
	if count > 0:
		string = string + ','
	name = k
	filename = v['filename']
	size = v['size']
	regions = v['regions']
	x_values = v['regions']

	string = string + '"' + name + '":{"filename":"' + filename + '","size":' + str(size) + ',"regions":['
	count2 = 0
	for i in x_values:
		if count2 > 0:
			string = string + ','
		dict1 = i['shape_attributes']
		
		for p in dict1:
			x_min = min(dict1['all_points_x'])
			x_max = max(dict1['all_points_x'])  
			y_min = min(dict1['all_points_y']) 
			y_max = max(dict1['all_points_y']) 
		string = string + '{"shape_attributes":{"name":"rect","x":'+str(x_min) + ',"y":' + str(y_min) + ',"width":' + str(int(float(x_max - x_min))) + ',"height":' + str(int(float(y_max - y_min))) + '},"region_attributes":{}}' 
		count2 = count2 +1
	string = string + '],"file_attributes":{}}'
	count = count +1
string = string + '}'

csv.write(string)
