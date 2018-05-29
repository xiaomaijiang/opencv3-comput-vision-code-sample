import cv2

image=cv2.imread('../images/1.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('MyImage',image)
cv2.waitKey()
cv2.destroyAllWindows()