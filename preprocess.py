import numpy as np
import cv2

def process_image (file):
	img = cv2.imread(file,0)

	img = cv2.resize(img, (500, 250)) 

	#Add blur
	cv2.GaussianBlur(img,(5,5),0)

	#reduces quality to simplify contourws
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (15,15))
	img = cv2.bitwise_not(img,img)

	#Grayscale
	_,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	#The dilated img copy is utilized for contours, we save the undilated version 
	undilated_image = img

	#Enlarge text 
	img_dilated = cv2.dilate(img, kernel, iterations=2)

	#Flip to white writing with black background 
	img = cv2.bitwise_not(img_dilated,img_dilated)

	#Contour equation
	m2, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# contours = sorted(contours, key=cv2.contourArea, reverse=True)

	#Sort contours left to right
	boundingBoxes = [cv2.boundingRect(c) for c in contours]
	(contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b:b[1][0], reverse=False))
	characters = []
	undilated_image = cv2.bitwise_not(undilated_image,undilated_image)
	# Draw contours
	for contour in contours:
	    
	    [x,y,w,h] = cv2.boundingRect(contour)

	    #Significant contours only
	    if (h>5):
	        cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),2)
	        cropped = undilated_image[y:y+h,x:x+w]
	        characters.append(cropped)	

	cv2.imshow('equation1',characters[1])
	cv2.imshow('equation2',characters[2])
	cv2.imshow('equation3',characters[3])
	cv2.imshow('equation4',characters[4])
	cv2.imshow('equation5',characters[5])

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return characters[1:]

if __name__ == "__main__":
    characters = process_image("equation1.jpg")