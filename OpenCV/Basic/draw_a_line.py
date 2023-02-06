import numpy as np
import cv2

#how big our image is going to be 
pic = np.zeros((500,500,3),dtype = 'uint8')

#(350,350) from where the line starts
#(500,350) to where the line ends
#(0,0,255) rgb colors
cv2.line(pic, (350,350), (500,350), (0,0,255))

cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
