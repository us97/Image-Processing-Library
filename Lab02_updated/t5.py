import numpy as np
import cv2
import os
os.chdir("E:\Drive\CEME Study\Semester 6\Digital Image Processing EC-312\Lab\Lab2(8-3-17)")
my=cv2.imread("super.jpg",0)
my1=cv2.resize(my,(512,512))
my2 = np.zeros((128,128))
for i in range(0,128):
    for j in range (0,128):
        my2[i,j]=my1[i*4,j*4]
cv2.imwrite("aaa.jpg",my2)
