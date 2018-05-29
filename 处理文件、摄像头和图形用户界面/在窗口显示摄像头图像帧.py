import cv2

click = False


def onMouse(event, x, y, flag, param):
    global click
    if event == cv2.EVENT_LBUTTONDBLCLK:
        click = True


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not click:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyAllWindows('MyWindow')
cameraCapture.release()
