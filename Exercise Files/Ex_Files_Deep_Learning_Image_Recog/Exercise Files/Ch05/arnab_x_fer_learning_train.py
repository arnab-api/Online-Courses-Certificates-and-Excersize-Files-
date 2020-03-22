#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:49:39 2019

@author: arnab
"""

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from pathlib import Path
import joblib

# Load data set
x_train = joblib.load("arnab_x_train.dat")
y_train = joblib.load("arnab_y_train.dat")

x_test = joblib.load("arnab_x_test.dat")
y_test = joblib.load("arnab_y_test.dat")


print(x_train.shape , y_train.shape)
print(x_test.shape , y_test.shape)


# Create a model and add layers
model = Sequential()

model.add(Flatten(input_shape=x_train.shape[1:]))

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=['accuracy']
)

# Train the model
model.fit(
    x_train,
    y_train,
    epochs=30,
    shuffle=True
)

# Save neural network structure
model_structure = model.to_json()
f = Path("arnab_model_structure.json")
f.write_text(model_structure)

# Save neural network's trained weights
model.save_weights("arnab_model_weights.h5")
