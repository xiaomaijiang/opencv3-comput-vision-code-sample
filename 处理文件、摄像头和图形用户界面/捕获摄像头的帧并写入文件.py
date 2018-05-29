import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30
size = (
    int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
videoWriter = cv2.VideoWriter(
    '../images/demo.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size
)
success, frame = cameraCapture.read()
numFramesRemaing = 10 * fps - 1
while success and numFramesRemaing > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaing -= 1
cameraCapture.release()
