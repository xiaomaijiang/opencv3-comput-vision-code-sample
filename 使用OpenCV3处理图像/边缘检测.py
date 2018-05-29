import cv2

image = cv2.imread('../images/1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('MyImage', cv2.Canny(image, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()
