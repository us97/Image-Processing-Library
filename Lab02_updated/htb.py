import numpy as np
import cv2
import os
os.chdir("E:\Drive\CEME Study\Semester 6\Digital Image Processing EC-312\Lab\Lab2(8-3-17)")
my=cv2.imread("ht.png",0)
r=4;

size=np.shape(my)
my1 = cv2.resize(my,(size[1]*r,size[0]*r))

cv2.imwrite("htbb.jpg",my1)
