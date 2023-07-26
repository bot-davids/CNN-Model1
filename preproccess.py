import numpy as np
from keras.preprocessing.image import ImageDataGenerator

#Program untuk melakukan proses dataset untuk keperluan training

#Direktori folder
TrainingImagePath = 'dataset/Training'
TestingImagePath = 'dataset/Testing'

#Menggunakan image data generator untuk melakukan preproses batch gambar yang sedikit dimodifikasi untuk keperluan training
train_datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        rescale=1./255)

#Image data generator untuk batch testing tanpa preproses
test_datagen = ImageDataGenerator(rescale=1./255)

#Mendapatkan training data batch dengan menjalankan fungsi image generator dari direktori
training_set = train_datagen.flow_from_directory(
        TrainingImagePath,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

#Testing data dari direktori
test_set = test_datagen.flow_from_directory(
        TestingImagePath,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

#Mendapatkan class setiap wajah berdasarkan id
test_set.class_indices
#lookup table untuk kebutuhan label
TrainClasses=training_set.class_indices
ResultMap={}
for faceValue,faceName in zip(TrainClasses.values(),TrainClasses.keys()):
    ResultMap[faceValue]=faceName
#Menyimpan tabel face
import pickle
with open("ResultsMap.pkl", 'wb') as fileWriteStream:
     pickle.dump(ResultMap, fileWriteStream)

#Memisahkan training set dalam bentuk x dan y
num_classes = training_set.num_classes
num_samples = len(training_set)
x_train = [] #x train merupakan bentuk gambar wajah
y_train = [] #y train merupakan bentuk label 

#Menjadikan batch x train ke bentuk grayscale
for i in range(num_samples):
    x_batch, y_batch = training_set[i]
    x_batch = np.dot(x_batch[..., :3],[0.2989,0.5870,0.1140])
    x_batch = np.expand_dims(x_batch, axis=-1)
    x_train.append(x_batch)
    y_train.append(y_batch)
x_train=np.concatenate(x_train, axis = 0)
y_train=np.concatenate(y_train, axis = 0)

#program sama untuk testing batch
num_samples = len(test_set)
x_test = []
y_test = []

for i in range(num_samples):
    x_batch, y_batch = test_set[i]
    x_batch = np.dot(x_batch[..., :3],[0.2989,0.5870,0.1140])
    x_batch = np.expand_dims(x_batch, axis=-1)
    x_test.append(x_batch)
    y_test.append(y_batch)
x_test=np.concatenate(x_test, axis = 0)
y_test=np.concatenate(y_test, axis = 0)
# The model will give answer as a numeric tag
# This mapping will help to get the corresponding face name for it
print("Mapping of Face and its ID",ResultMap)