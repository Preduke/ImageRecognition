# Annotation Box mit Integer Werten (z.B. 1023 524 1131 570 1) in Form von xmin ymin xmax ymax wie z.B. bei carpk in yolo Format (z.B. 0 0.84140625 0.7597222222222223 0.084375 0.0638888888888889) umwandeln. 

1. Annotations Files (txt Files) in Unterordner "Annotations" kopieren. 
2. Unterordner "output" erstellen, in dem Ergebnis gespeichert wird.
3. JPG Files in Pfad, in dem Python-File ausgeführt wird, kopieren (wird benötigt um Filegröße auszulesen) und Zeile 81 bei Windows wie folgt anpassen: "img_path = str('%s\%s.jpg'%(wd, os.path.splitext(txt_name)[0]))".
ODER
3. Unterordner "Images" erstellen und JPG Files einfügen. Achtung evtl. muss trotzdem Zeile 81 angepasst werden, je nach Betriebssystem ist "/" oder "\ gefordert.
4. Python-File ausführen

