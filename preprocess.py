import numpy as np
import cv2

def horizontal_dilation(img):
    r, c = img.shape
    parts = []
    for i in range(c):
        pixel_vals = img[:,i]
        parts.append(pixel_vals)
        if max(pixel_vals) < 50 or  np.sum(pixel_vals >200)<1 : 
                parts.append(pixel_vals)
                parts.append(pixel_vals)
                parts.append(pixel_vals)
                parts.append(pixel_vals)
    return np.transpose(np.asarray(parts))

def shadow_removal (img):
     #Shadow Removal
    rgb_planes = cv2.split(img)

    result_norm_planes = []
    #Process plane
    for plane in rgb_planes:

        img_dilated = cv2.dilate(plane, np.ones((7,7), np.uint8))
        img_blurred = cv2.medianBlur(img_dilated, 21)
        img_absdiff = 255 - cv2.absdiff(plane, img_blurred)
        img_norm = cv2.normalize(img_absdiff, None,alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_norm_planes.append(img_norm)

    img = cv2.merge(result_norm_planes)
    return img

def process_image (file):
    img = cv2.imread(file,0)
    img = cv2.resize(img, (1240,331)) 
    img = shadow_removal (img)
    # Add blur
    cv2.GaussianBlur(img,(5,5),0)

    #reduces quality to simplify contourws
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (40,40))
    
    #Grayscale
    _,img = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    img = cv2.bitwise_not(img,img)

    #Add border in case that text is against an edge of the picture
    img = cv2.copyMakeBorder(img,top=10,bottom=10,left=10,right=10,borderType = cv2.BORDER_CONSTANT,value=[0,0,0])
    img = horizontal_dilation (img)
    img = np.ascontiguousarray(img, dtype=np.uint8)

    #The dilated img copy is utilized for contours, we save the undilated version 
    undilated_image = img

    #Enlarge text 
    img_dilated = cv2.dilate(img, kernel, iterations=1)
    img_dilated = cv2.erode(img_dilated,cv2.getStructuringElement(cv2.MORPH_CROSS, (2,2)))

    #Flip to white writing with black background 
    img = cv2.bitwise_not(img_dilated,img_dilated)
    img = cv2.bitwise_not(img)

    #Contour equation
    m2, contours, hierarchy = cv2.findContours(img,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.CHAIN_APPROX_SIMPLE)

    #Sort contours left to right
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b:b[1][0], reverse=False))
    characters = []

    #Img saved should be black text, so we inverse colors for array to be saved 
    undilated_image = cv2.bitwise_not(undilated_image,undilated_image)

    # Draw contours

    for contour in contours:
        
        [x,y,w,h] = cv2.boundingRect(contour)

        #Significant contours only
        if h>10:
            cv2.rectangle(img_dilated,(x,y),(x+w,y+h),(100,100,100),1)
            if np.sum(undilated_image[y:y+h,x:x+w] >100) > 2000:
                cropped = undilated_image[y:y+h,x:x+w]
                characters.append(cropped)  

    # DEBUG: 
    # Uncomment to show the full equation and the first 6 characters spliced
    # cv2.imshow('Full Equation',undilated_image)
    # cv2.imshow('equation0',characters[0])
    # cv2.imshow('equation1',characters[1])
    # cv2.imshow('equation2',characters[2])
    # cv2.imshow('equation3',characters[3])
    # cv2.imshow('equation4',characters[4])
    # cv2.imshow('equation5',characters[5])
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return characters

if __name__ == "__main__":
    characters = process_image("equation1.jpg")