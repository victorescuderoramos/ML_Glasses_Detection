import cv2
from skimage.io import imread
import os
import numpy as np

def read_data(path, im_size):
    X = []
    Y = []

    #Iteramos sobre cada imagen:
    for file in os.listdir(path):
        
        #Leemos imagen:
        image = imread(path + file)

        #Preprocesamos las imágenes:
        image = cv2.resize(image, (im_size, im_size))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = image[40:80,20:105]
        ret, thresh = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)

        #Guardamos las imágenes ya preprocesadas en nuestra variable X:
        X.append(thresh)
        
        #Hacemos conteo de imágenes de gafas y de no gafas
        category = file.split(' ')[0]

        if category == 'gafas':
            Y.append(1)
        else:
            Y.append(0)
        
    return np.array(X), np.array(Y)