import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("SysLog8",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
