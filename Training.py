from keras import callbacks
from Model import model
from preproccess import x_train, y_train, x_test, y_test
from preproccess import num_classes
import pickle

#Program untuk menjalankan training

classifier = model((64,64,1),num_classes) #Mendapatkan model dari program model.py dan memberikan argumen shape
#Model dinamakan classifier

#Menyimpan Weight model dalam format h5 untuk digunakan keperluan testing
checkpoint = callbacks.ModelCheckpoint('trained_model.h5', monitor='accuracy',
                                           save_best_only=True, save_weights_only=True, verbose=1)

classifier.fit(x_train, y_train,                            #Mengambil training batch dan memasukkan ke model untuk melakukan training
             batch_size=32,
             epochs=32,
             validation_data=(x_test,y_test),               #Menggunakan testing batch untuk validasi training
             shuffle=True,callbacks=[checkpoint])
             
#Menampilkan jumlah wajah yang telah di training di terminal
print("\n [INFO] " + str(num_classes) + " faces trained. Exiting Program")

#Menyimpsn model dalam bentuk pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(classifier, file)
print("\n [INFO] " + str(num_classes) + " faces trained. Exiting Program")