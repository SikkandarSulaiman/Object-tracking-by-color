import cv2
import numpy as np

def noCallBack(nothing):
    pass

def findThreshold(img):
    
    cv2.namedWindow('image')

    cv2.createTrackbar('Upper H', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower H', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Upper S', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower S', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Upper V', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower V', 'image', 0, 255, noCallBack)

    cv2.setTrackbarPos('Lower H', 'image', 255)
    cv2.setTrackbarPos('Lower S', 'image', 255)
    cv2.setTrackbarPos('Lower V', 'image', 255)

    while(1):
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == 13:
            break

        ru = cv2.getTrackbarPos('Upper H','image')
        gu = cv2.getTrackbarPos('Upper S','image')
        bu = cv2.getTrackbarPos('Upper V','image')
        rl = cv2.getTrackbarPos('Lower H','image')
        gl = cv2.getTrackbarPos('Lower S','image')
        bl = cv2.getTrackbarPos('Lower V','image')

        obj_u = np.array([ru, gu, bu])
        obj_l = np.array([rl, gl, bl])

        _, frame = img.read()
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        filtered = cv2.inRange(hsvFrame, obj_u, obj_l)

        cv2.putText(filtered, 'Filter the object and press Enter to fix thresholds',
                    (0,20), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,0,0), 1)
        
        cv2.imshow('image', filtered)

    cv2.destroyAllWindows()
    return [obj_u, obj_l]

if __name__ == '__main__':
    img = cv2.VideoCapture(0)
    findThreshold(img)
    img.release()
