import numpy as np
import cv2

pic = cv2.imread('image.jpg')

cols = pic.shape[1]
rows = pic.shape[0]

#translation matrix
#150 pixels to right in x axis
#70 pixels down in y axis
#put -150 for left and -70 for up
M = np.float32([[1,0,150],[0,1,70]])
shifted = cv2.warpAffine(pic, M, (cols,rows))

cv2.imshow('shifted', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
