import cv2
from que import Queue
from track import findThreshold

Q=Queue()

img = cv2.VideoCapture(0)

[lowerThresh, upperThresh], [erosion, dilation] = findThreshold(img)

while True:
    _, frame = img.read()
    h, w, _ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    obj = cv2.inRange(hsv, lowerThresh, upperThresh)
    obj = cv2.erode(obj, None, iterations=erosion)
    obj = cv2.dilate(obj, None, iterations=dilation)
    cv2.imshow("debug", obj)
    c_obj, _ = cv2.findContours(obj, 1, 2)

    for c in c_obj:
        M = cv2.moments(c)
        if M["m00"] == 0:
            M["m00"]=1
        dX = int(M["m10"] / M["m00"])
        dY = int(M["m01"] / M["m00"])
        cv2.drawContours(frame, c_obj, -1, (0,255,255), 3)
        (x, y), r = cv2.minEnclosingCircle(c)
        cv2.circle(frame, (int(x), int(y)), int(r), (0,0,255), 3)
        Q.enq((dX, dY))
        Q.deq
        for i in xrange(0,20):
            try:
                cv2.line(frame, Q.ret(i), Q.ret(i+1), (255,0,0), 3)
            except IndexError:
                pass
        cv2.putText(frame, str(int(x))+" "+str(int(y)),
                    (dX-10,dY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (55,120,255), 2)
    
    cv2.putText(frame, 'Press enter to tune threshold values',
                    (0, h-5), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,255,255), 1)
    cv2.imshow("cont",frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 13:
        cv2.destroyAllWindows()
        [lowerThresh, upperThresh], [erosion, dilation] = findThreshold(img,
                    [upperThresh, lowerThresh], erosion, dilation)

img.release()
cv2.destroyAllWindows()



