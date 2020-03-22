#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:36:53 2019

@author: arnab
"""
import keras
from keras.datasets import cifar10
from pathlib import Path
import numpy as np
import joblib
from keras.preprocessing import image
from keras.applications import vgg16

# Load data set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize data set to 0-to-1 range
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Normalize image data to 0-to-1 range
x_train = vgg16.preprocess_input(x_train)
x_test = vgg16.preprocess_input(x_test)

print(x_train.shape , y_train.shape)
print(x_test.shape , y_test.shape)

# Load a pre-trained neural network to use as a feature extractor
pretrained_nn = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

# Extract features for each image (all in one pass)
features_x_train = pretrained_nn.predict(x_train)
features_x_test = pretrained_nn.predict(x_test)


# Save the array of extracted features to a file
joblib.dump(features_x_train, "arnab_x_train.dat")
joblib.dump(features_x_test, "arnab_x_test.dat")

# Save the matching array of expected values to a file
joblib.dump(y_train, "arnab_y_train.dat")
joblib.dump(y_test, "arnab_y_test.dat")


print("DATASET SAVED IN DAT FORMAT")


