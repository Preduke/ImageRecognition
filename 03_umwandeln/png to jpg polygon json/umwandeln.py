# Anpassen der json File, wenn diese auf Grundlage von nicht jpg-Dateien erstellt wurden.
# 
# 1. Bilder im .jpg Format und im "alten" Format in den Folder kopieren.
# 2. json File der Bilder des "alten" Formats in den Folder kopieren
# 3. umwandeln.py ausführen

import os, sys, random
import xml.etree.ElementTree as ET
from glob import glob
import pandas as pd
from shutil import copyfile
import re
import json


# Hier die Endung der alten Bilder angeben:
endung = 'png'
pics_old = glob('./*.'+endung)

# Hier den Namen der json File anpassen: 
with open('via_region_data.json') as f:
	data = json.load(f)
	string = json.dumps(data)

for file in pics_old:
	file2 = file.replace(endung, 'jpg')
	
# Jetzt lesen wir pro Bild die Filesize beider Dateien aus uns ersetzen diese
	size_old = os.path.getsize(file)
	size_new = os.path.getsize(file2)
	string = string.replace(str(size_old),str(size_new))	
	string = string.replace(str(endung),'jpg')

# Dann alles in der OUTPUT abspeichern
download_dir ="OUTPUT.json"
csv = open(download_dir, "w")
csv.write(string)

