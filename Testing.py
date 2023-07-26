import numpy as np
import cv2
import pickle
import pandas as pd
import requests

#Program untuk melakukan testing label dan hasil training
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('ResultsMap.pkl', 'rb') as file:
    ResultMap = pickle.load(file)

classifier = model #Mendapatkan model
#Menambahkan weight yang telah disimpan dari proses training
classifier.load_weights('trained_model.h5')

def GetName(key, df):
    Idloc=df.index[df['FaceID']==key][0]
    elemen = df.at[Idloc,'Name']
    return elemen
def GetNPM(key, df):
    Idloc=df.index[df['FaceID']==key][0]
    elemen = df.at[Idloc,'NPM']
    return elemen
Database = pd.read_csv('Data_Mahasiswa.csv')

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (50,205,50)
video_capture = cv2.VideoCapture(0)

def start():
    print('here')
    ret = True

    while ret:
        #read frame by frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,
        minNeighbors=5,
        minSize=(30, 30)) #Mendapatkan bounding box wajah menggunakan haarcascade

        #Memproses bagian wajah saja
        for (x, y, w, h) in faces:
            #Memproses gambar wajah ke format untuk menjalankan testing ke model
            face_img = gray[y:y+h,x:x+w]
            face_img = cv2.resize(face_img, (64,64))
            face_img = np.expand_dims(face_img, axis=-1)
            face_img = np.expand_dims(face_img, axis=0)
            face_img = face_img / 255.0

            prediction = classifier.predict(face_img)

            #menampilkan hasil prediksi secara real time
            label = ResultMap[np.argmax(prediction[0])]
            Name= str(GetName(label,Database))
            NoPM = int(GetNPM(label,Database))
            NoPM = str(NoPM)


            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, Name, (x-10,y-50), font, 1, font_color, 2)
            cv2.putText(frame, NoPM, (x-10,y-10), font, 1, font_color, 2)
        cv2.imshow("Android_cam", frame) #Menampilkan kamera dalam window

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    cv2.destroyAllWindows()
    
    
start()