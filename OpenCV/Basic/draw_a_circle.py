import numpy as np
import cv2

#how big our image is going to be 
pic = np.zeros((500,500,3),dtype = 'uint8')

color = (255,0,255)

#circle centre
#50 radius

cv2.circle(pic, (250,250), 50, color)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
