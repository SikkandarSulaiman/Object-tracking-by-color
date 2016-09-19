import cv2
import numpy as np
from que import Queue
Q=Queue()


obj_l = np.array([39,26,0])
obj_u = np.array([62,255,255])

img=cv2.VideoCapture(0)

while True:
    _, frame = img.read()
    h,w,_=frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    obj = cv2.inRange(hsv, obj_l, obj_u)
    obj = cv2.erode(obj, None, iterations=1)
    obj = cv2.dilate(obj, None, iterations=1)
    cv2.imshow("debug",obj)
    c_obj,_ = cv2.findContours(obj, 1, 2)

    for c in c_obj:
        M = cv2.moments(c)
        if M["m00"] == 0:
            M["m00"]=1
        dX = int(M["m10"] / M["m00"])
        dY = int(M["m01"] / M["m00"])
        cv2.drawContours(frame, c_obj, -1, (0,255,255), 3)
        (x,y),r = cv2.minEnclosingCircle(c)
        cv2.circle(frame, (int(x),int(y)), int(r), (0,0,255), 3)
        Q.enq((dX,dY))
        Q.deq
        for i in range(0,20):
            try:
                cv2.line(frame,Q.ret(i),Q.ret(i+1),(255,0,0),3)
            except IndexError:
                pass
        cv2.putText(frame, str(int(x))+" "+str(int(y)),
                    (dX-10,dY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (55,120,255),2)

##        px,py = Q.ret(5)
##        nx,ny = Q.ret(0)
##        del_x = nx-px
##        del_y = ny-py
##        if abs(del_x)>2 and abs(del_y)>2:
##            end = ((del_x)*100,(del_y)*100)
##        elif abs(del_y)>2 and not abs(del_x)>2:
##            end = (nx,(del_y)*100)
##        elif abs(del_x)>2 and not abs(del_y)>2:
##            end = ((del_x)*100,ny)
##        else:
##            end = (nx,ny)
##
##        cv2.line(frame, (nx,ny), end, (0,255,0), 3)
            
        
        
    cv2.imshow("cont",frame)

    if cv2.waitKey(1) == 27:
        break

img.release()
cv2.destroyAllWindows()



