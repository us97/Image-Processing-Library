import numpy as np
import cv2 as cv
import blob as b
import csv as cs
import math as m


arrytemp1 = cv.imread("img/hw3_leaf_training_1.jpg", 0)
arrytemp2 = cv.imread("img/hw3_leaf_training_2.jpg", 0)
arrytemp3 = cv.imread("img/hw3_leaf_training_3.jpg", 0)
arrytemp4 = cv.imread("img/hw3_leaf_training_4.jpg", 0)
arrytemp5 = cv.imread("img/hw3_leaf_training_5.jpg", 0)
assignment = cv.imread("img/hw3_leaf_testing_1.jpg", 0)

obj1 = b.Blob()
obj2 = b.Blob()
obj3 = b.Blob()
obj4 = b.Blob()
obj5 = b.Blob()

data1 = obj1.extractfeature(arrytemp1)
data2 = obj2.extractfeature(arrytemp2)
data3 = obj3.extractfeature(arrytemp3)
data4 = obj4.extractfeature(arrytemp4)
data5 = obj4.extractfeature(arrytemp5)

array1 = obj1.features()
array2 = obj2.features()
array3 = obj3.features()
array4 = obj4.features()
array5 = obj5.features()

csvinputdata = [array1, array2, array3, array4, array5]
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
# resdata = res.findobjects(assignment,csvoutputdata)
res.extractfeature(assignment)
resdata = res.features()
print(resdata)

# labels = []
# feat = np.array(csvoutputdata, float)
# # distancelist = []
# # # for i in feat:
# # #     data = m.sqrt(m.pow(i[0] - resdata[0], 2) + m.pow(i[1] - resdata[1], 2) + m.pow(i[2] - resdata[2], 2))
# # #     distancelist.append(data)
# # #     # print(distancelist)
# # #     # print(distancelist.index(min(distancelist)) + 1)
# # #     labels.append(distancelist.index(min(distancelist)) + 1)
# # #     distancelist.clear()