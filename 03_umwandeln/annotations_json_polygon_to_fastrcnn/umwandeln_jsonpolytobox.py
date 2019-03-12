# json Poylon File aus VIA in den Default Ordner
# Python Skript ausfuehren


import json
from pprint import pprint

download_dir ="output_FILE.json"
csv = open(download_dir, "w")

with open('Input_FILE2.json') as f:
	data = json.load(f)

string = ''
count = 0
for (k,v) in data.items():
	if count > 0:
		string = string
	name = k
	filename = v['filename']
	size = v['size']
	regions = v['regions']
	x_values = v['regions']

	##string = string
	count2 = 0
	for i in x_values:
		if count2 > 0:
			string = string
		dict1 = i['shape_attributes']
		
		for p in dict1:
			x_min = min(dict1['all_points_x'])
			x_max = max(dict1['all_points_x'])  
			y_min = min(dict1['all_points_y']) 
			y_max = max(dict1['all_points_y']) 
		string = string + filename + ','+str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ',car\n' 
		count2 = count2 +1
	count = count +1
string = string

csv.write(string)
