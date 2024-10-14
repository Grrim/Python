# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:51:04 2021

@author: Grim
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolution(image, kernel):
    heigthI, widthI = image.shape
    heightK, widthK = kernel.shape
    frame = ((widthK) // 2)
    image = np.pad(image, frame, mode='symmetric')
    output = np.zeros((heigthI, widthI))
    for x in range(frame, heigthI + frame):
        for y in range(frame, widthI + frame):
            output[y-1, x-1] = (image[y-frame: y+frame+1, x-frame: x+frame+1]*kernel).sum()
    output = (output/255)
    return output

def Progowanie(img):
    height, width = img.shape
    Pn = np.zeros((height,width), np.uint8)
    mean = 0
    for i in range(height):
        for j in range(width):
            mean += img[i][j]
    T0 = mean/(height*width)
    T1 = 0;
    for i in range(height):
        for j in range(width):
            if (img[i][j] >= T0):
                Pn[i][j] = 1
            else:
                Pn[i][j] = 0
    Pn = (Pn*255)
    return Pn

input_image = cv2.imread('litery.png')
image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

Roberts1 = np.array(([0, 0, 0], [0, -1, 0], [0, 1, 0]), dtype="int")
Roberts2 = np.array(([0, 0, 0], [0, -1, 1], [0, 0, 0]), dtype="int")
Roberts3 = np.array(([0, 0, 0], [0, 0, 1], [0, -1, 0]), dtype="int")
Roberts4 = np.array(([0, 0, 0], [0, 1, 0], [0, 0, -1]), dtype="int")

Prewitt1 = np.array(([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]), dtype="int")
Prewitt2 = np.array(([-1, -1, -1], [0, 0, 0], [1, 1, 1]), dtype="int")
Prewitt3 = np.array(([0, 1, 1], [-1, 0, 1], [-1, -1, 0]), dtype="int")
Prewitt4 = np.array(([-1, -1, 0], [-1, 0, 1], [0, 1, 1]), dtype="int")

Laplace = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), dtype = "int")

Sobel1 = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]), dtype="int")
Sobel2 = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]), dtype="int")
Sobel3 = np.array(([0, 1, 2], [-1, 0, 1], [-2, -1, 0]), dtype="int")
Sobel4 = np.array(([-2, -1, 0], [-1, 0, 1], [0, 1, 2]), dtype="int")

Kircha1 = np.array(([-3, -3, 5], [-3, 0, 5], [-3, -3, 5]), dtype="int")
Kircha2 = np.array(([-3, 5, 5], [-3, 0, 5], [-3, -3, -3]), dtype="int")
Kircha3 = np.array(([5, 5, 5], [-3, 0, -3], [-3, -3, -3]), dtype="int")
Kircha4 = np.array(([5, 5, -3], [5, 0, -3], [-3, -3, -3]), dtype="int")
Kircha5 = np.array(([5, -3, -3], [5, 0, -3], [5, -3, -3]), dtype="int")
Kircha6 = np.array(([-3, -3, -3], [5, 0, -3], [5, 5, -3]), dtype="int")
Kircha7 = np.array(([-3, -3, -3], [-3, 0, 3], [5, 5, 5]), dtype="int")
Kircha8 = np.array(([-3, -3, -3], [-3, 0, 5], [-3, 5, 5]), dtype="int")
                                               
KK1 = Kircha1
KK2 = Kircha2
KK3 = Kircha3
KK4 = Kircha4                                          
KK5 = Kircha5
KK6 = Kircha6
KK7 = Kircha7
KK8 = Kircha8        
Kircha1C = convolution(image, KK1)
Kircha2C = convolution(image, KK2)
Kircha3C = convolution(image, KK3)
Kircha4C = convolution(image, KK4)
Kircha5C = convolution(image, KK5)
Kircha6C = convolution(image, KK6)
Kircha7C = convolution(image, KK7)
Kircha8C = convolution(image, KK8)

KS1 = Sobel1
KS2 = Sobel2
KS3 = Sobel3
KS4 = Sobel4
Sobel1C = convolution(image, KS1)
Sobel2C = convolution(image, KS2)
Sobel3C = convolution(image, KS3)
Sobel4C = convolution(image, KS4)

KL = Laplace
Laplace1C = convolution(image, KL)

KP1 = Prewitt1
KP2 = Prewitt2
KP3 = Prewitt3
KP4 = Prewitt4
Prewitt1C = convolution(image, KP1)
Prewitt2C = convolution(image, KP2)
Prewitt3C = convolution(image, KP3)
Prewitt4C = convolution(image, KP4)

KR1 = Roberts1
KR2 = Roberts2
KR3 = Roberts3
KR4 = Roberts4
Roberts1C = convolution(image, KR1)
Roberts2C = convolution(image, KR2)
Roberts3C = convolution(image, KR3)
Roberts4C = convolution(image, KR4)

a = np.sqrt(np.square(Roberts1C) + np.square(Roberts2C) + np.square(Roberts3C) + np.square(Roberts4C))
b = Laplace1C
c = np.sqrt(np.square(Prewitt1C) + np.square(Prewitt2C) + np.square(Prewitt3C) + np.square(Prewitt4C))
d = np.sqrt(np.square(Sobel1C) + np.square(Sobel2C) + np.square(Sobel3C) + np.square(Sobel4C))
e = np.sqrt(np.square(Kircha1C) + np.square(Kircha2C) + np.square(Kircha3C) + np.square(Kircha4C) + np.square(Kircha5C) + np.square(Kircha6C) + np.square(Kircha7C) + np.square(Kircha8C))
cv2.imshow("Oryginalny", input_image)
cv2.imshow("Roberts", a)
cv2.imshow("Laplace", b)
cv2.imshow("Pawitt", c)
cv2.imshow("Sobel", d)
cv2.imshow("Kircha", e)
cv2.waitKey(0)
cv2.destroyAllWindows()

binary1 = Progowanie(a)
binary2 = Progowanie(b)
binary3 = Progowanie(c)
binary4 = Progowanie(d)
binary5 = Progowanie(e)
cv2.imshow('Obraz Roberts', binary1)
cv2.imshow('Obraz Laplace', binary2)
cv2.imshow('Obraz Pawitt', binary3)
cv2.imshow('Obraz Sobel', binary4)
cv2.imshow('Obraz Kircha', binary5)
cv2.waitKey(0)
cv2.destroyAllWindows()


edges = cv2.Canny(image,100,200)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
