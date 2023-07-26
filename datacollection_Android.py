import cv2
import os
import requests
import numpy as np
import imutils
import pandas as pd

#Program untuk mengumpulkan data wajah dengan membuka camera Android

url = "http://192.168.1.3:8080/shot.jpg" #url untuk menghubungkan koneksi ipcam android

def check_folder(folder_name):
    if os.path.exists(folder_name):
        return True
    else: return False

#Metode deteksi wajah menggunakan opencv Haarcascade
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#directory folder
path = 'dataset' 
i=0

while(True):
    trainingpath = path + "/Training/User"+ str(i)
    if check_folder(trainingpath)==True:
        i+=1
    else:
        break
face_id=i
print ("Face id :",face_id)
Database = pd.read_csv('Data_Mahasiswa.csv')

Name=str(input("Input Nama : "))
Numer=str(input("Input NPM : "))
fid="face"+str(face_id)
df_add={'FaceID':[fid],'Name':[Name],'NPM':[Numer]}
df_add=pd.DataFrame(df_add)
Database=pd.concat([Database, df_add], ignore_index=True)
Database.to_csv('Data_Mahasiswa.csv',index=False,sep=",")

   
os.mkdir(trainingpath)
testpath = path + '/Testing/User' + str(face_id) #menggunakan id untuk penamaan directory
os.mkdir(testpath)

#Program mengambil dan mengumpulkan gambar dari camera
count = 0
while(True):
    img_resp = requests.get(url) #Membaca gambar dari alamat url yang terhubung
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1280, height=720)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    #Mendapatkan gambar dari bounding box Haarcascade
    for (x,y,w,h) in faces:
        count += 1
        cv2.rectangle(img, (x,y), (x+w+50,y+h+50), (255,0,0), 2)     
        id=str(face_id)
        n=str(count)

        #Menyimpan gambar-gambar ke folder training dan testing
        face = img[y:y+h,x:x+w]
        
        cv2.imwrite("%s/User.%s.%s.jpg"%(trainingpath,id,n),face)
        if count<=12:
            cv2.imwrite("%s/User.%s.%s.jpg"%(testpath,id,n),face)
        cv2.imshow("Android_cam", img)
        
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cv2.destroyAllWindows()

