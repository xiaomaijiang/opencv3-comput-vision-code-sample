import cv2
import numpy
from scipy import ndimage

image = cv2.imread('../images/1.png', cv2.IMREAD_GRAYSCALE)
kernel_3x3 = numpy.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])
k3 = ndimage.convolve(image, kernel_3x3)

kernel_5x5 = numpy.array([
    [-1, -1, -1, -1, -1],
    [-1, 1, 1, 1, -1],
    [-1, 2, 4, 2, -1],
    [-1, 1, 2, 1, -1],
    [-1, -1, -1, -1, -1],
])
cv2.imshow('MyImage', k3)
cv2.waitKey()

k5 = ndimage.convolve(k3, kernel_5x5)
cv2.imshow('MyImage', k5)
cv2.waitKey()

blurred = cv2.GaussianBlur(image, (11, 11), 0)
g_hpf = image - blurred
cv2.imshow('MyImage', g_hpf)
cv2.waitKey()

cv2.destroyAllWindows()
