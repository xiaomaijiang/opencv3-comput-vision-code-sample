import cv2
import numpy as np

image = cv2.imread('../images/1.png', cv2.IMREAD_GRAYSCALE)

ret,thresh=cv2.threshold(image,127,255,0)
img,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
color=cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
image=cv2.drawContours(color,contours,-1,(0,255,0),2)

cv2.imshow('MyImage', color)
cv2.waitKey()
cv2.destroyAllWindows()
