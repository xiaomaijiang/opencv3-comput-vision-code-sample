import cv2

image=cv2.imread('../images/1.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('../images/2.png',image)