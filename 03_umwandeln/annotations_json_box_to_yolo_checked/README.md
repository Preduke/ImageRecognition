# Annotation json Box in Yolo Files umwandeln.

Aus den Box Annotations werden Yolo Annotation Files erstellt. 
1. Annotations Box (rect) json File (via_region_data.json) in Folder kopieren. Achtung: Unbedingt nur die Annotations verwenden und nicht das json-Projekt. Wenn das json-Projekt verwendet wird, muss der Code ab Zeile 21 wie folgt angepasst werden: 
    > imgmetadata = data["_via_img_metadata"]
    
    > for (k,v) in imgmetadata.items():
    
2. Alle Bilder (jpg) aus dem Annotation-json-File in einen neuen Ordner namens "pics" kopieren (wir benötigen die Auflösung der Bilder). Falls das Format nicht jpg ist, muss der Code angepasst werden.
3. Python-File ausführen.
