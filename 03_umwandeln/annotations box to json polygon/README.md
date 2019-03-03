# Annotation Box in JSON Polygon umwandeln.

1. Annotations Files (txt Files) in Folder kopieren. 
2. JPG Files in Folder kopieren (wird benötigt um Filegröße auszulesen) 
3. Python-File ausführen. Achtung: 	Zeile 24 "filename = file.split('/')[-1].split('.')[0] + '.jpg'" bei Ausführung unter Windows ersetzen mit:
> filename = file.split('\\')[-1].split('.')[0] + '.jpg' 
