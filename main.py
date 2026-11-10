import cv2
import numpy as np
#load image
image=cv2.imread("image.png")
if image is None:
    print("image not found")
    exit()
#display the original image
cv2.imshow("original image",image)
#color conversions
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",gray)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)#color concentated image
cv2.imshow("hsv image",hsv)
#image rotation
clockwise=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Clockwise rotation",clockwise)
anticlockwise=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Anticlockwise rotation",anticlockwise)
#verical flipping 
vertical=cv2.flip(image,0)
cv2.imshow("vertical flip",vertical)
#crop an image
cropped_section=image[0:200,0:200]
cv2.imshow("Cropped section",cropped_section)
#increase brightness
bright=np.clip(image.astype(np.int16)+50,0,255).astype(np.uint8)
cv2.imshow("Bright image",bright)
#Decrease the brightness
dark=np.clip(image.astype(np.int16)-50,0,255).astype(np.uint8)
cv2.imshow("Dark image",dark)
#Increase contrast
contrast=cv2.convertScaleAbs(image,alpha=1.5,beta=0)
cv2.imshow("High contrast Image",contrast)
#horizontal flipping
horizontal=cv2.flip(image,1)
cv2.imshow("Horizontal flip",horizontal)
#negative image
negative=225-image
cv2.imshow("Negative image",negative)
#keep the window open
cv2.waitKey(0)
cv2.destroyAllWindows()