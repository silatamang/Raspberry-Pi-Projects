import numpy as np
import cv2

pic = cv2.imread('image.jpg')

kernal = 3

median = cv2.medianBlur(pic, kernal)

#removes the noise around images
#cv2.imshow('median blur',pic)
cv2.imshow('median blur',median)

cv2.waitKey(0)

cv2.destroyALlWindows()

