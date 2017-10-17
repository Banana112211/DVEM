import cv2
import Ensure_dir
import os
import time
import Write_Logfile
def videoaufzeichnung(video_wdth,video_hight,eingang,dir_path,queue,num_frames=1000,sync="ja",qual=90):
    import time
    #1.Step: Festlegung der Bildeigenschaften
    cap = cv2.VideoCapture(eingang)
    cap.set(3,video_wdth) # wdth
    cap.set(4,video_hight) #hight 
    timestamp = int(time.time()) # generiert einen Unix Timestamp. 
    #Kann mit der Funktion  datetime.datetime.utcfromtimestamp(timestamp) in normale Zeit konvertiert werden
    #==============
    #2 Step: Aendern die aktuellen Arbeitspath
    print dir_path
    os.chdir(dir_path) #Zuerst wird die cwd auf das aktuelle File gesetzt    
    #3.Step: Erstellt einen Order zum Abspeichern der Bilder
    folder_name="Kamera "+str(eingang)+"; videowdth "+str(video_wdth)+"; videohight "+str(video_hight)
    Ensure_dir.ensure_dir(folder_name)
    os.chdir(dir_path+"/"+folder_name)
    cwd= dir_path+"/"+folder_name #Das ist der Name in der 
    #4.Step: erstelle kamera.txt mit spalten ueberschrift
    os.chdir(dir_path) 
    Write_Logfile.logfile_schreiben('"Input";"Wdth";"hight";"Timestamp";"Number";"Date";"Key"',str(folder_name))
    #5.Step: Kamera benoentig etwas aufwaermzeit, daher wird While-Loop bis success= true ist
    success,image = cap.read()    
    while success==False:
        import time
        time.sleep(1)
        success,image = cap.read()    

    #6.Step: Erstellen und Abspeichern der Bilder
    print timestamp
    start = time.time()
    #6.1: Abfrage ob eine Synchronisierung notwenidig ist
    if sync=="ja":
        for i in range(0,num_frames):
    #        0.Step: Holt aus der quere den aktuellen Zeitstemple
            key_simulator=queue.get()
            now=time.asctime()
            timestamp = time.time() #ansonsten wird die Zeit nicht aktualisiert
            success,image = cap.read()
            #message= str(folder_name)+"; "+str(timestamp)+"; Nummer "+str(i)+"; "+str(now) #Diese Zeile fuer Ubuntu
            message= str(folder_name)+"; "+str(timestamp)+"; Nummer "+str(i)#DIESE ZEILE fuer windows verwenden 
            cv2.imwrite(cwd+"/"+message+".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), qual]) #Speichert frame mit einer absoluten Addresierung
            message2= str(message)+";"+str(key_simulator)
            os.chdir(dir_path) 
            Write_Logfile.logfile_schreiben(message2,str(folder_name))
            i += 1
    else:
        for i in range(0,num_frames):
    # 0.Step: Holt aus der quere den aktuellen Zeitstemple
            key_simulator=queue
            now=time.asctime()
            timestamp = time.time() #ansonsten wird die Zeit nicht aktualisiert
            success,image = cap.read()
            #message= str(folder_name)+"; "+str(timestamp)+"; Nummer "+str(i)+"; "+str(now) #Diese Zeile fuer Ubuntu
            message= str(folder_name)+"; "+str(timestamp)+"; Nummer "+str(i)+"; "#DIESE ZEILE fuer windows verwenden 
            cv2.imwrite(cwd+"/"+message+".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), qual]) #Speichert frame mit einer absoluten Addresierung
            message2= str(message)+";"+str(key_simulator)
            os.chdir(dir_path) 
            Write_Logfile.logfile_schreiben(message2,str(folder_name))
            i += 1
    print message
    end = time.time()
    seconds = end - start
    #Berechnung der fps
    fps  = num_frames / seconds;
    #3.Step: Nun wird die Liste in das Log.txt geschrieben
    os.chdir(dir_path) 
    #Step: Schreibt die berechnete fps in txt-file
    message3= ", {0} seconds, {1} num_frames, {2} fps".format(seconds,num_frames,fps)
    Write_Logfile.logfile_schreiben(message3,str(folder_name))
    print "sucessful {0}".format(success)
#===Test 
#Einstellungn=[(176, 144),(320,240),(352,288),(432,240),(544,288),(640,480),(800,448),(864,480) ,(960, 544),(960, 720),(1184, 656), (1280, 960)]
#dir_path = os.path.dirname(os.path.realpath(__file__))
#for element in Einstellungn:
#    videoaufzeichnung(element[0],element[1],0,dir_path)
