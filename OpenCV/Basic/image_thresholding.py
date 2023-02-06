import cv2
import numpy as np

#first load in grayscale
pic = cv2.imread('image.jpg',0)

threshold_value = 10

#THRESH_BINARY_INV for opposite
(T_value,binary_threshold) = cv2.threshold(pic,threshold_value, 255,cv2.THRESH_BINARY)

cv2.imshow('threshold',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
