# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:05:46 2021

@author: Grim
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def Filtracja(img, maska):
    dft = cv2.dft(img, flags = cv2.DFT_COMPLEX_OUTPUT)
    fft = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(fft[:,:,0],fft[:,:,1]))
    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.show()
    maskowanie = fft*maska
    ifft = np.fft.ifftshift(maskowanie)
    widmo = cv2.idft(ifft)
    widmo = cv2.magnitude(widmo[:,:,0], widmo[:,:,1])
    return widmo

def convolution(image, kernel):
    heigthI, widthI = image.shape
    heightK, widthK = kernel.shape
    frame = ((widthK) // 2)
    image = np.pad(image, frame, mode='symmetric')
    output = np.zeros((heigthI, widthI))
    for x in range(frame, heigthI + frame-1):
        for y in range(frame, widthI + frame-1):
            output[y-1, x-1] = (image[y-frame: y+frame+1, x-frame: x+frame+1]*kernel).sum()
    output = (output/255)
    dft = cv2.dft(output, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.show()
    return output


image = np.float32(cv2.imread('original.png', 0))
image1 = cv2.imread('original.png',0)
#image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
height, width = image.shape
heightK = (height//2)
widthK = (width//2)
GPMask = np.ones((height,width,2))
GPMask[heightK-500:heightK+500, widthK-500:widthK+500] = 0
DPMask = np.zeros((height,width,2))
DPMask[heightK-500:heightK+500, widthK-500:widthK+500] = 1
t1 = time.time()
FiltracjaDP = Filtracja(image, DPMask)
t2 = time.time()
print(t2-t1)
t1 = time.time()
FiltracjaGP = Filtracja(image, GPMask)
t2 = time.time()
print(t2-t1)
plt.imshow(image, cmap = 'gray')
plt.show()
plt.imshow(FiltracjaGP, cmap = 'gray')
plt.show()
plt.imshow(FiltracjaDP, cmap = 'gray')
plt.show()

kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
kernel2 = np.ones((5,5),np.float32)/25
kernel = kernel2/sum(kernel2)
t1 = time.time()
Splot1 = convolution(image1, kernel)
t2 = time.time()
print(t2-t1)
plt.imshow(Splot1, cmap = 'gray')
plt.show()

kernel = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), dtype = "int")
t1 = time.time()
Splot1 = convolution(image1, kernel)
t2 = time.time()
print(t2-t1)
cv2.imshow('Contours3', Splot1)
cv2.waitKey()
cv2.destroyAllWindows()


def Scaling(img, maska):
    dft = cv2.dft(img, flags = cv2.DFT_COMPLEX_OUTPUT)
    fft = np.fft.fftshift(dft)
    magnitude_spectrum = (1/2)*np.log(cv2.magnitude(fft[:,:,0],fft[:,:,1]))
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.show()
    maskowanie = magnitude_spectrum
    ifft = np.fft.ifftshift(maskowanie)
    widmo = cv2.idft(ifft)
    magnitude_spectrum = np.log(cv2.magnitude(widmo[:,:,0], widmo[:,:,1]))
    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.show()
    widmo = cv2.magnitude(widmo[:,:,0], widmo[:,:,1])
    return widmo

#ES = Scaling(image, GPMask)
#plt.imshow(ES, cmap = 'gray')
#plt.show()