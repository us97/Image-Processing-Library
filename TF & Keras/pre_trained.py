import cv2
import numpy as np

from keras.applications.inception_resnet_v2 import InceptionResNetV2 as incpt # Importing the model

# Methods of MobileNet for making changing the input to the required shape and then decoding the output
from keras.applications.inception_resnet_v2 import decode_predictions, preprocess_input


image_1_path = "F:/SEMESTER 06/DIP/CNN/TF & Keras/Data/cat.jpg"
image_2_path = "F:/SEMESTER 06/DIP/CNN/TF & Keras/Data/moon.jpg"
image_3_path = "F:/SEMESTER 06/DIP/CNN/TF & Keras/Data/space_shuttle.jpg"

# Reading the images
image_1 = cv2.resize(cv2.imread(image_1_path, 1), (299, 299))
image_2 = cv2.resize(cv2.imread(image_2_path, 1), (299, 299))
image_3 = cv2.resize(cv2.imread(image_3_path, 1), (299, 299))
# Creating a copy of the images for displaying purpose
image_1_copy = image_1
image_2_copy = image_2
image_3_copy = image_3


# Pre-processing the input
image_1 = np.expand_dims(image_1, axis=0)
image_2 = np.expand_dims(image_2, axis=0)
image_3 = np.expand_dims(image_3, axis=0)

image_1 = preprocess_input(image_1)
image_2 = preprocess_input(image_2)
image_3 = preprocess_input(image_3)

# Loading the model
my_model = incpt(weights='imagenet')

# Model Summary
# my_model.summary()


cv2.imshow("Cat", image_1_copy)
cv2.waitKey(0)
print("Predicted:", decode_predictions(my_model.predict(image_1), top=3)[0])


cv2.imshow("Moon", image_2_copy)
cv2.waitKey(0)
print("Predicted:", decode_predictions(my_model.predict(image_2), top=3)[0])


cv2.imshow("Space Shuttle", image_3_copy)
cv2.waitKey(0)
print("Predicted:", decode_predictions(my_model.predict(image_3), top=3)[0])



