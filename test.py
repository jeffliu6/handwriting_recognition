

import numpy as np
import cv2

img = cv2.imread('equation1.jpg',0)
img = cv2.resize(img, (500, 250)) 

#Add blur
cv2.GaussianBlur(img,(5,5),0)

#reduces quality to simplify contourws
kernel = np.ones((12,12), np.uint8) 
img = cv2.erode(img, kernel, iterations=1) 

#Grayscale
_,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Flip to white writing with black background 
img = cv2.bitwise_not(img,img)

#Contour equation
m2, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Draw contours
for contour in contours:
    
    [x,y,w,h] = cv2.boundingRect(contour)

    if (h>13):
    
    	cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),2)


#Show
cv2.imshow('equation',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  