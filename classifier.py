from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.models import model_from_json
import numpy as np
import os
import matplotlib.pyplot as plt
from constants import LABELS

"""
[classify(img)] is a string representation of the numpy array representation of an image of handwritting [img]
"""
def classify(img):
    # load saved model
    json_file = open('model.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model.h5")
    model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])   
    ret_str = ""
    for m in model.predict_classes(img): 
        c = LABELS[m]
        if c == "div" or c == "forward_slash":
            c =  "/"
        elif c == "times":
            c = "*"  
        ret_str += str(c)
    return ret_str