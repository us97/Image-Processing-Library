import numpy as np
import cv2 as cv
import Blob as b
import csv as cs
import math as m


# arrytemp1 = cv.imread("a1.bmp", 0)
arrytemp2 = cv.imread("a2.bmp", 0)
arrytemp3 = cv.imread("b2.bmp", 0)
# arrytemp4 = cv.imread("a4.bmp", 0)
assignment = cv.imread("b3.bmp", 0)

# obj1 = b.Blob()
obj2 = b.Blob()
obj3 = b.Blob()
# obj4 = b.Blob()
# data1 = obj1.extractfeature(arrytemp1)
data2 = obj2.extractfeature(arrytemp2)
data3 = obj3.extractfeature(arrytemp3)
# data4 = obj4.extractfeature(arrytemp4)
# array1 = obj1.features()
array2 = obj2.features()
array3 = obj3.features()
# array4 = obj4.features()

csvinputdata = [array2, array3]
with open('person.csv','w') as csvfile:
    writer=cs.writer(csvfile)
    writer.writerows(csvinputdata)
csvfile.close()

csvoutputdata = []
with open('person.csv', 'r') as csvFile:
    reader = cs.reader(csvFile)
    for row in reader:
        csvoutputdata.append(row)
csvFile.close()
print(csvoutputdata)

res = b.Blob()
resdata = res.findobjects(assignment,csvoutputdata)
print(resdata)