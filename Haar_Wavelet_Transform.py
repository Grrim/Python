# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:25:48 2021

@author: Grim
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
import cv2 

image = cv2.imread('test.bmp', 0)
plt.imshow(image, cmap = 'gray')
plt.show()

def Haar(falka, poziom):
    haar = pywt.wavedec2(image, falka, level = poziom)
    haar[0] = haar[0]/np.abs(haar[0]).max()
    for i in range(poziom):
        haar[i+1] = [j/np.abs(j).max() for j in haar[i+1]]
        
    return haar

def Haar_zerowanie(falka, poziom):
    haar = pywt.wavedec2(image, falka, level = poziom)
    haar[0] = haar[0]/np.abs(haar[0]).max()
    cA, (cH, cV, cD) = haar
    heigth, width = cD.shape
    print(cD)
    print(np.mean(cD))
    for i in range(heigth):
        for j in range(width):
            cD[i][j] = cV[50][50]
    #print(cD)
    for i in range(poziom):
        haar[i+1] = [j/np.abs(j).max() for j in haar[i+1]]

    return haar
 

hr, fk = pywt.coeffs_to_array(Haar('haar', 1))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.show()

hr, fk = pywt.coeffs_to_array(Haar('haar', 2))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.xlim([0, 237.5])
plt.ylim([237.5, 0])
plt.show()

hr, fk = pywt.coeffs_to_array(Haar('haar', 3))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.xlim([0, 118.75])
plt.ylim([118.75, 0])
plt.show()

hr, fk = pywt.coeffs_to_array(Haar('haar', 4))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.xlim([0, 59.375])
plt.ylim([59.375, 0])
plt.show()

hr, fk = pywt.coeffs_to_array(Haar('haar', 5))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.xlim([0, 29.6875])
plt.ylim([29.6875, 0])
plt.show()

plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.show()

hr, fk = pywt.coeffs_to_array(Haar_zerowanie('haar', 1))
plt.imshow(hr, cmap = 'gray', vmin = -0.4, vmax = 1.5)
plt.show()