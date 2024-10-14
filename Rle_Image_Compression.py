# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:04:29 2021

@author: Grim
"""

import cv2
import numpy as np
import sys

image = cv2.imread('123.png')
cv2.imshow('Image',image)
cv2.waitKey(0)
rows, cols,channels = image.shape
print(image.size)
image1D = image.flatten()

def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def RLE(img):
    quantityRLE = []
    bitsRLE = []
    DecodedRLE = []
    licznik_powtórzeń = 1
    print(img.size)
    #Encode
    if(len(image.shape) == 3):
        for i in range(img.shape[0]-1):
            if (licznik_powtórzeń == 1):
                bitsRLE.append(img[i])
            if img[i] == img[i+1]:
                licznik_powtórzeń += 1
            elif img[i] != img[i+1]:
                quantityRLE.append(licznik_powtórzeń)
                licznik_powtórzeń = 1  
            if i == img.shape[0] - 2:
                bitsRLE.append(img[i])
                quantityRLE.append(licznik_powtórzeń)   
        print(len(bitsRLE))
        
        #Decode
        for i in range(len(quantityRLE)):
            for j in range(quantityRLE[i]):
                DecodedRLE.append(bitsRLE[i])
        DecodedRLE = np.reshape(DecodedRLE,(rows,cols,channels))
        
    #Encode
    elif(len(image.shape) == 2):
        for i in range(img.shape[0]-1):
            if (licznik_powtórzeń == 1):
                bitsRLE.append(img[i])
            if img[i] == img[i+1]:
                licznik_powtórzeń += 1
            elif img[i] != img[i+1]:
                quantityRLE.append(licznik_powtórzeń)
                licznik_powtórzeń = 1  
            if i == img.shape[0] - 2:
                bitsRLE.append(img[i])
                quantityRLE.append(licznik_powtórzeń) 
                
        #Decode
        for i in range(len(quantityRLE)):
            for j in range(quantityRLE[i]):
                DecodedRLE.append(bitsRLE[i])
        DecodedRLE = np.reshape(DecodedRLE,(rows,cols))

    CompresionPercent = round(len(bitsRLE)/img.shape[0]*100, 2)
    print("Stopień kompresji: ", str(CompresionPercent) + '%')
    print(DecodedRLE.size)
    cv2.imshow('Decoded Image', DecodedRLE) 
    cv2.waitKey(0)

RLE(image1D)
