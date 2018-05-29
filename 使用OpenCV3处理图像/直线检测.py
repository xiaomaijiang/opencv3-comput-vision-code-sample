import cv2
import numpy

image = cv2.imread('../images/1.png')
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 50, 120)

lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 100, 20, 5)
for obj in lines:
    for x1, y1, x2, y2 in obj:
        cv2.line(image, (x1, y1), (x2, y2),(0,255,0),2)

cv2.imshow('img',edges)
cv2.waitKey()

cv2.imshow('img',lines)
cv2.waitKey()
cv2.destroyAllWindows()
