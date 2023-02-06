import numpy as np
import cv2

pic = cv2.imread('image.jpg')

#image dimension
cols = pic.shape[1]
rows = pic.shape[0]

#part of image we want to rotate
center = (cols/2,rows/2)
angle = 90

#1 is for scale with which we want to rotate
M = cv2.getRotationMatrix2D(center, angle,1)

rotate = cv2.warpAffine(pic, M, (cols,rows))

cv2.imshow('rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
