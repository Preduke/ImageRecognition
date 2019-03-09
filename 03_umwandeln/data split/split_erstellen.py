import json
import os
from PIL import Image
from pprint import pprint
import pandas as pd
from glob import glob
import numpy as np
import shutil

# Erst alle Bilder im Folder zählen:
pcount = 0
bilder = glob('./*.jpg')
for file in bilder:
	
	pcount = pcount + 1

tcount = int(round(pcount * 0.2,0))

testcount = tcount
traincount = pcount - tcount
print('Picture Count:', pcount)
print('Train Count:', traincount)
print('Test Count:', testcount)

#Erst Testdaten
image_ids = np.random.choice(bilder, testcount)
for image_id in image_ids:
	# erst die bilder kopieren
	path_old = image_id
	path_new = './test/' + path_old[2:]
	shutil.move(path_old, path_new)
	# Dann txt files
	path_old =  path_old[:-4]+'.txt'
	path_new = './test/' + path_old[2:]
	shutil.move(path_old, path_new)

# Der Rest sind dann Traindaten
bilder = glob('./*.jpg')
for file in bilder:
	path_old = file
	path_new = './train/' + path_old[2:]
	shutil.move(path_old, path_new)
	path_old =  path_old[:-4]+'.txt'
	path_new = './train/' + path_old[2:]
	shutil.move(path_old, path_new)

