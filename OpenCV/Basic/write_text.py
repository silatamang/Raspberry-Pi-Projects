import numpy as np
import cv2

#how big our image is going to be 
pic = np.zeros((500,500,3),dtype = 'uint8')

#Font can be different, can look up from opencv documentation
font= cv2.FONT_HERSHEY_DUPLEX

#(100,100) where we want to place the text
#3 is the size of text
#rgb color
#4 is the thickness
#type of line through which text is going to be drawn, can be found or changed through opencv documentation

cv2.putText(pic, 'Code Okie', (100,100), font, 3, (255,255,255), 4, cv2.LINE_8)

cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
