import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import cv2

Image = cv2.imread(r"C:\Users\grzes\OneDrive\Pulpit\SM_Lab04\0013.jpg")
plt.imshow(Image)
plt.show()

rgb = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()

lab = cv2.cvtColor(Image, cv2.COLOR_BGR2LAB)
plt.imshow(lab)
plt.show()

ycrcb = cv2.cvtColor(Image, cv2.COLOR_BGR2YCrCb)
plt.imshow(ycrcb)
plt.show()

ycrcb = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
plt.imshow(ycrcb)
plt.show()

def Quantization(img, n):
    arr = np.asarray(img,dtype=np.uint8)
    x, y, z = arr.shape
    arrn = arr.reshape(x*y, z)
    
    k_means = KMeans(n_clusters=n)
    k_means.fit(arrn)
    y_kmeans = k_means.predict(arrn)

    centroids = k_means.cluster_centers_
    labels = k_means.labels_
    
    centr = centroids[labels]
    conversion = centr.reshape(x,y,z)

    plt.imshow(conversion/255)
    plt.show()
    
    ax = plt.subplot(projection = '3d')
    ax.scatter(arrn[:, 0], arrn[:, 1], arrn[:,2], c=y_kmeans)
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    a,b,d = conversion[:,:,0], conversion[:,:,1], conversion[:,:,2];
       
    ax.scatter(a, b, d, c = y_kmeans)
    plt.show(); 
    
    return conversion
    
a = Quantization(rgb, 4)

def Brightness(img):
    d = 0
    a = np.array(img, np.int)
    height, width = a.shape
    mn = height*width*255
    for x in range(1, height):
        for y in range(1, width):
            d += a[x][y]
    return (1/mn)*d

def Contrast(img):
    d = 0
    a = np.array(img, np.int)
    height, width = a.shape
    mn = height*width*255
    J = Brightness(img)
    for x in range(1, height):
        for y in range(1, width):
            d += (np.sqrt((a[x][y]) - (J))**2)
            #d += (np.sqrt((a[x][y]) - (J)))
    return (1/mn)*d

