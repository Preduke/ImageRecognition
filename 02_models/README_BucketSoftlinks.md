1. Unter /home/valeria_reifschneider/unicorn-analytics-bucket/ ist der "unicorn-analytics-bucket"-Bucket eingebunden.
Achtung kann bei Neustart verschwunden sein: Befehl zum mounten im Ordner /home/valeria_reifschneider ausführen: 
$ gcsfuse unicorn-analytics-bucket ./unicorn-analytics-bucket/
Anleitung zum Einbinden von Buckets: https://cloud.google.com/storage/docs/gcs-fuse

2. Für das Training / Testen der Modelle, kann auf bestimmten Ordner in Bucket ein Softlink erstellt werden. Man muss also nicht den Bucket-Inhalt in die VM kopieren!
Dazu erst "ln -s " dann den Pfad zum Ordner im Bucket und danach den Zielpfad eingeben (Verlinkung zu Bucket Ordner).
Vorteil: Alles was im Bucket geändert wird (gelöscht, neu hochgeladen etc. ist dadurch, dass alles nur Verlinkungen sind, direkt überall auf dem gleichen Stand).
Z. B. $sudo ln -s /home/valeria_reifschneider/unicorn-analytics-bucket/yolo/ ./obj

3. Danach Modell starten.
Z. B. Yolo im Ordner /home/valeria_reifschneider/darknet mit dem Befehl 
$./darknet detector test data/obj.data yolo-obj.cfg ./yolo-obj_4000_old.weights


./darknet detector train data/obj.data yolo-obj.cfg ./backup/yolo-obj_last.weights -gpus 0,1,2,3

./darknet detector map data/obj.data yolo-obj2.cfg ./backup_old/yolo-obj_4000.weights
Dauer: 41 Minuten 24 Sekunden

./darknet detector calc_anchors data/obj.data -num_of_clusters 9 -width 416 -height 416
11:25-
