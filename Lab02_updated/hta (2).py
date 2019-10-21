import numpy as np
import cv2
import os
os.chdir("E:\Drive\CEME Study\Semester 6\Digital Image Processing EC-312\Lab\Lab2(8-3-17)")
my=cv2.imread("ht.jpg",0)
size=np.shape(my)
my1 = np.zeros((size[0],size[1]))
for i in range(0,np.int16(size[0]*4)):
    for j in range (0,np.int16(size[1]*4)):
        my1[i,j]=my[np.int16(i/4),int16(j/4)]
cv2.imwrite("htaa.jpg",my2)
