import numpy as np
import cv2
import os
os.chdir("E:\Drive\CEME Study\Semester 6\Digital Image Processing EC-312\Lab\Lab2(8-3-17)")
siz = 500
b8=250
my=np.ones((siz,siz))
for i in range(0,siz):
    for j in range(0,siz):
        my[i,j]=255             
for i in range(0,b8):
    for j in range(0,b8):
        my[i,j]=0
for i in range(siz-b8,siz):
    for j in range(0,b8):
         my[i,j]=0     
for i in range(0,b8):
    for j in range(siz-b8,siz):
         my[i,j]=0      
for i in range(siz-b8,siz):
    for j in range(siz-b8,siz):
        my[i,j]=0
cv2.imshow("dg",my)
cv2.imwrite("f4dotblack.jpg",my)
