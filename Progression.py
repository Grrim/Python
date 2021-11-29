# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 15:18:57 2021

@author: Grim
"""

import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

Image = cv2.imread(r"C:\Users\grzes\OneDrive\Pulpit\coins2 (1).png", 0)
cv2.imshow('Oryginalny obraz', Image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(Image)

plt.hist(Image.ravel(),256,[0,256])
plt.show()

def Progowanie(img):
    height, width = img.shape
    Pn = np.zeros((height,width), np.uint8)
    mean = 0
    for i in range(height):
        for j in range(width):
            mean += img[i][j]
    print(mean)
    T0 = mean/(height*width)
    print("Wartosc progu:", T0)
    T1 = 0;
    for i in range(height):
        for j in range(width):
            if (img[i][j] >= T0):
                Pn[i][j] = 1
            else:
                Pn[i][j] = 0
    Pn = (Pn*255)
    return Pn
        
    
binary = Progowanie(Image)
cv2.imshow('Obraz progowanie', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(binary.ravel(),256,[0,256])
plt.show()

height,width = Image.shape
im = np.zeros((height,width),np.uint8)
noise = cv2.randn(im,(0),(255))
NoiseImage = cv2.add(Image, noise)
print(noise)
cv2.imshow('Zaszumiony obraz', NoiseImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(NoiseImage.ravel(),256,[0,256])
plt.show()

binary = Progowanie(NoiseImage)
cv2.imshow('Obraz zaszumiony progowanie', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(binary.ravel(),256,[0,256])
plt.show()


