import cv2
import numpy as np

cam = cv2.VideoCapture(0)
width = 640
height = 480
cam.set(3,width)
cam.set(4,height)

def empty(z):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',width,0)
cv2.resizeWindow('Trackbars', 640, 500)
cv2.createTrackbar('Hue mini', 'Trackbars', 0, 179, empty)
cv2.createTrackbar('Hue max', 'Trackbars', 24, 179, empty)
cv2.createTrackbar('Hue mini2', 'Trackbars', 169, 179, empty)
cv2.createTrackbar('Hue max2', 'Trackbars', 179, 179, empty)
cv2.createTrackbar('Sat mini', 'Trackbars', 93, 255, empty)
cv2.createTrackbar('Sat max', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('Val mini', 'Trackbars', 99, 255, empty)
cv2.createTrackbar('Val max', 'Trackbars', 255, 255, empty)



while True:
    zzz, img = cam.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('img', img)
    cv2.moveWindow('img',0,0) 

    hMin = cv2.getTrackbarPos('Hue mini', 'Trackbars')
    hMax = cv2.getTrackbarPos('Hue max', 'Trackbars')
    hMin2 = cv2.getTrackbarPos('Hue mini2', 'Trackbars')
    hMax2 = cv2.getTrackbarPos('Hue max2', 'Trackbars')
    sMin = cv2.getTrackbarPos('Sat mini', 'Trackbars')
    sMax = cv2.getTrackbarPos('Sat max', 'Trackbars')
    vMin = cv2.getTrackbarPos('Val mini', 'Trackbars')
    vMax = cv2.getTrackbarPos('Val max', 'Trackbars')

    lower = np.array([hMin,sMin,vMin])
    upper = np.array([hMax,sMax,vMax])
    lower2 = np.array([hMin2,sMin,vMin])
    upper2 = np.array([hMax2,sMax,vMax])

    mask = cv2.inRange(imgHsv,lower,upper)
    mask2 = cv2.inRange(imgHsv,lower2,upper2)
    maskComp = mask | mask2
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    imgResult2 = cv2.bitwise_and(img, img, mask=maskComp)

    cv2.imshow('res', imgResult2)
    cv2.moveWindow('res',width+640,0)
    # cv2.imshow('res2', imgResult2)
    # cv2.moveWindow('res2',width+640,height)
    cv2.imshow('mask', maskComp)
    cv2.moveWindow('mask',0,height)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break