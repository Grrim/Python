# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:25:08 2021

@author: Grim
"""

import numpy as np
import cv2

Disk3 = np.array(([0, 1, 0],[1, 1, 1],[0, 1, 0]), dtype="int")
Disk5 = np.array(([0, 0, 1, 0, 0],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[0, 0, 1, 0, 0]), dtype="int")
Disk7 = np.array(([0, 0, 0, 1, 0, 0, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[0, 0, 0, 1, 0, 0, 0]), dtype="int")
Square3 = np.array(([1, 1, 1],[1, 1, 1],[1, 1, 1]), dtype="int")
Square5 = np.array(([1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]), dtype="int")
Square7 = np.array(([1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1]), dtype="int")

def Dilate(img, kernel):
    height, width = img.shape
    heightK, widthK = kernel.shape
    output = np.array(img)
    frame = ((widthK)//2)
    for i in range(1):
        border = np.pad(output, frame, mode='symmetric')
        for i in range(1, height):
            for j in range(1, width):
                if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) >= 255:
                    output[i, j] = 255
    return output
 
def Erode(img, kernel):
    height, width = img.shape
    heightK, widthK = kernel.shape
    frame = ((widthK)//2)
    output = np.array(img)
    for i in range(1):
        border = np.pad(output, frame, mode='symmetric')
        for i in range(1, height):
            for j in range(1, width):
                if (heightK == 7):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(5*(frame*frame)+frame):
                            output[i, j] = 0     
                    elif np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame+frame+1)+1):
                        output[i, j] = 0
                elif (heightK == 5):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(9*(frame)+frame):
                            output[i, j] = 0
                    elif np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame+frame)+1):
                        output[i, j] = 0
                elif (heightK == 3):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(9*(frame)):
                            output[i, j] = 0
                    else:
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame)+1):
                            output[i, j] = 0
    return output

def Contours(img, kernel):
    height, width = img.shape
    heightK, widthK = kernel.shape
    frame = ((widthK)//2)
    output = np.array(img)
    for i in range(1):
        border = np.pad(output, frame, mode='symmetric')
        for i in range(1, height):
            for j in range(1, width):
                if (heightK == 7):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(5*(frame*frame)+frame):
                            output[i, j] = 0     
                    elif np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame+frame+1)+1):
                        output[i, j] = 0
                elif (heightK == 5):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(9*(frame)+frame):
                            output[i, j] = 0
                    elif np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame+frame)+1):
                        output[i, j] = 0
                elif (heightK == 3):
                    if (kernel[-1][-1] == 1):
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(9*(frame)):
                            output[i, j] = 0
                    else:
                        if np.sum(kernel * border[i-1:i+frame+frame, j-1:j+frame+frame]) < 255*(4*(frame)+1):
                            output[i, j] = 0
    return img-output
 
    
def Close(img, kernel):
	dilate = Dilate(img, kernel)
	output = Erode(dilate, kernel)
	return output
 

def Open(img, kernel):
    erode = Erode(img, kernel)
    output = Dilate(erode, kernel)
    return output
 
image = cv2.imread('test1.png', 0)
ret,thresh = cv2.threshold(image,127,255,0)
contoursIMG = Contours(image, Square7)
dilateIMG = Dilate(image, Square7)
erodeIMG = Erode(image, Square7)
closeIMG = Close(image, Square7)
openIMG = Open(image, Square7)
cv2.imshow("contours", contoursIMG)
cv2.imshow("dilate", dilateIMG)
cv2.imshow("erode", erodeIMG)
cv2.imshow("close", closeIMG)
cv2.imshow("open", openIMG)
cv2.imshow("Original", image)

ret,thresh = cv2.threshold(contoursIMG,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)

contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
drawing = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
for i in range(len(contours)):
    color = (255, 255, 255)
    cv2.drawContours(drawing, contours, i, color, 1, cv2.LINE_8, hierarchy, 0)
cv2.imshow('Contours', drawing)

cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)

erosion = cv2.morphologyEx(image, cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)))

new = contoursIMG - drawing
cv2.imshow('Contours3', new)
cv2.waitKey()
cv2.destroyAllWindows()