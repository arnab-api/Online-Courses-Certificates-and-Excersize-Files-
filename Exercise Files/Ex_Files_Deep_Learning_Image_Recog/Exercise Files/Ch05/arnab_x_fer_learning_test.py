#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:07:23 2019

@author: arnab
"""

from keras.models import model_from_json
from pathlib import Path
from keras.preprocessing import image
import numpy as np
from keras.applications import vgg16
import joblib


# Load the json file that contains the model's structure
f = Path("arnab_model_structure.json")
model_structure = f.read_text()

# Recreate the Keras model object from the json data
model = model_from_json(model_structure)

# Re-load the model's trained weights
model.load_weights("arnab_model_weights.h5")

x_test = joblib.load("arnab_x_test.dat")
y_test = joblib.load("arnab_y_test.dat")


# Given the extracted features, make a final prediction using our own model
results = model.predict(x_test)

# Since we are only testing one image with possible class, we only need to check the first result's first element
print(results[5])
print(y_test[5])