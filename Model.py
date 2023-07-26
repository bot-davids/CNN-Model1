from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense,Flatten

#Program membentuk model untuk dipakai di program lain

#Fungsi membangun model
def model(inputShape,num_classes):
    model=Sequential()
    #Menambahkan lapisan konvolusi dengan batch size 32 dan kernel size 3,3
    model.add(Conv2D(32, (3, 3), activation = 'relu', input_shape=inputShape, strides=(1,1)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    #Menambahkan lapisan konvolusi dengan batch size 64
    model.add(Conv2D(64, (3, 3), activation = 'relu', strides=(1,1)))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(128, (3, 3), activation = 'relu', strides=(1,1)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    #Menambahkan lapisan Flatten 
    model.add(Flatten())
    #Menambahkan lapisan Dense
    model.add(Dense(256, activation = 'relu'))
    model.add(Dense(128, activation = 'relu'))
    #Menambahkan lapisan Dense akhir dan menggunakan aktivasi softmax untuk keperluan prediksi
    model.add(Dense(num_classes, activation='softmax'))
    
    #Menggabungkan lapisan menjadi model dengan karakteristik berikut.
    model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

              
    model.summary()
    return model
    