import cv2

img = cv2.imread('../images/1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
kp = surf.detect(gray, None)

img = cv2.drawKeypoints(gray, kp, img)

cv2.imshow("img", img)

k = cv2.waitKey(0)
if k & 0xff == 27:
    cv2.destroyAllWindows()