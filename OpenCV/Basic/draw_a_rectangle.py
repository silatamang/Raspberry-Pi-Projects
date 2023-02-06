import numpy as np
import cv2

#how big our image is going to be 
pic = np.zeros((500,500,3),dtype = 'uint8')

#(0,0) coordinates from where we draw a rectangle
#From (0,0) coordinates to (500,150) x and y coordinates
#(123,200,98) RGB Color codes
#3 is for the three channels of RGB colors
#lineType for either dotted or straight line
#shift
cv2.rectangle(pic, (0,0), (500,150), (123,200,98),3, lineType=8, shift=0)

cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
