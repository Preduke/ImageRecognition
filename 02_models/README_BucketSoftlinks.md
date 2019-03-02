1. Unter /home/valeria_reifschneider/unicorn-analytics-bucket/ ist der "unicorn-analytics-bucket"-Bucket eingebunden. Anleitung zum Einbinden von Buckets: https://cloud.google.com/storage/docs/gcs-fuse

2. Für das Training / Testen der Modelle, kann auf bestimmten Ordner in Bucket ein Softlink erstellt werden. Man muss also nicht den Bucket-Inhalt in die VM kopieren!
Dazu erst "ln -s " dann den Pfad zum Ordner im Bucket und danach den Zielpfad eingeben (Verlinkung zu Bucket Ordner).
Vorteil: Alles was im Bucket geändert wird (gelöscht, neu hochgeladen etc. ist dadurch, dass alles nur Verlinkung sind, direkt überall auf dem gleichen Stand).
Z. B. $sudo ln -s /home/valeria_reifschneider/unicorn-analytics-bucket/yolo/ ./obj

3. Danach Modell starten.
Z. B. Yolo im Ordner /home/jupyter/darknet mit dem Befehl 
$./darknet detector test data/obj.data yolo-obj.cfg ./yolo-obj_4000_old.weights