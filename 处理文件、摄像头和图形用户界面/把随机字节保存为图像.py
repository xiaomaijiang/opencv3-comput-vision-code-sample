import os
import cv2
import numpy

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
grayImage=flatNumpyArray.reshape(300,400)

cv2.imwrite('../images/randomGray.png',grayImage)

rgbImage=flatNumpyArray.reshape(100,400,3)
cv2.imwrite('../images/randomRGB.png',rgbImage)
