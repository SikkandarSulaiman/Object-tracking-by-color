import cv2
import numpy as np

def noCallBack(nothing):
    pass

def findThreshold(img, thresh=[[255,255,255], [0,0,0]], erosion=0, dilation=0):
    
    cv2.namedWindow('image')

    cv2.createTrackbar('Upper H', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower H', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Upper S', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower S', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Upper V', 'image', 0, 255, noCallBack)
    cv2.createTrackbar('Lower V', 'image', 0, 255, noCallBack)

    cv2.createTrackbar('Erode', 'image', 0, 20, noCallBack)
    cv2.createTrackbar('Dilate', 'image', 0, 20, noCallBack)

    cv2.setTrackbarPos('Upper H', 'image', thresh[1][0])
    cv2.setTrackbarPos('Upper S', 'image', thresh[1][1])
    cv2.setTrackbarPos('Upper V', 'image', thresh[1][2])
    cv2.setTrackbarPos('Lower H', 'image', thresh[0][0])
    cv2.setTrackbarPos('Lower S', 'image', thresh[0][1])
    cv2.setTrackbarPos('Lower V', 'image', thresh[0][2])

    cv2.setTrackbarPos('Erode', 'image', erosion)
    cv2.setTrackbarPos('Dilate', 'image', dilation)

    while True:

        upperH = cv2.getTrackbarPos('Upper H','image')
        upperS = cv2.getTrackbarPos('Upper S','image')
        upperV = cv2.getTrackbarPos('Upper V','image')
        lowerH = cv2.getTrackbarPos('Lower H','image')
        lowerS = cv2.getTrackbarPos('Lower S','image')
        lowerV = cv2.getTrackbarPos('Lower V','image')
        erosion = cv2.getTrackbarPos('Erode', 'image')
        dilation = cv2.getTrackbarPos('Dilate', 'image')

        upperThresh = np.array([upperH, upperS, upperV])
        lowerThresh = np.array([lowerH, lowerS, lowerV])

        _, frame = img.read()
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsvFiltered = cv2.inRange(hsvFrame, upperThresh, lowerThresh)
        eroded = cv2.erode(hsvFiltered, None, iterations=erosion)
        dilated = cv2.dilate(eroded, None, iterations=dilation)

        cv2.putText(dilated, 'Filter the object and press Enter to fix thresholds',
                    (0,20), cv2.FONT_HERSHEY_PLAIN, 1.3, (255,0,0), 1)
        
        cv2.imshow('image', dilated)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == 13:
            break

    cv2.destroyAllWindows()
    return [[upperThresh, lowerThresh],[erosion, dilation]]

if __name__ == '__main__':
    img = cv2.VideoCapture(0)
    findThreshold(img)
    img.release()
