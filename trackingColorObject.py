import cv2
import numpy as np

hMin = 0
hMax = 0
sMin = 0
sMax = 0
vMin = 0
vMax = 0
hMin2 = 0
hMax2 = 0
ar = 0
x=0
y=0

def tr1(val):
    global hMin
    hMin = val
def tr2(val):
    global hMax
    hMax = val
def tr3(val):
    global sMin
    sMin = val
def tr4(val):
    global sMax
    sMax = val
def tr5(val):
    global vMin
    vMin = val
def tr6(val):
    global vMax
    vMax = val
def tr7(val):
    global hMin2
    hMin2 = val
def tr8(val):
    global hMax2
    hMax2 = val

def ar(val):
    global ar
    ar = val

cv2.namedWindow('tracks')
cv2.resizeWindow('tracks',400,500)
cv2.createTrackbar('hMin', 'tracks', 59, 179, tr1)
cv2.createTrackbar('hMax', 'tracks', 96, 179, tr2)
cv2.createTrackbar('hMin2', 'tracks', 65, 179, tr7)
cv2.createTrackbar('hMax2', 'tracks', 83, 179, tr8)

cv2.createTrackbar('sMin', 'tracks', 46, 255, tr3)
cv2.createTrackbar('sMax', 'tracks', 255, 255, tr4)
cv2.createTrackbar('vMin', 'tracks', 67, 255, tr5)
cv2.createTrackbar('vMax', 'tracks', 255, 255, tr6)

cv2.createTrackbar('area', 'tracks', 4100, 10000, ar)

cam = cv2.VideoCapture(0)
width = 640
height = 480



while True:
    zzz, img = cam.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    lower2 = np.array([hMin2, sMin, vMin])
    upper2 = np.array([hMax2, sMax, vMax])

    mask = cv2.inRange(imgHsv, lower, upper)
    mask2 = cv2.inRange(imgHsv, lower2, upper2)

    myMask = mask | mask2
    contours, junk = cv2.findContours(myMask, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img, contours,-1,(0,0,255),3)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area>=ar:
            #cv2.drawContours(img, [contour], 0, (0,0,255),3)
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            print(x,y)

    combo = cv2.bitwise_and(img, img, mask=myMask)

    cv2.imshow('img', img)
    cv2.moveWindow('img', int(x+x*1.5), int(y*1.3))
    cv2.imshow('mask', myMask)
    cv2.moveWindow('mask', width, 0)
    cv2.imshow('combo', combo)
    cv2.moveWindow('combo', int(2*width), 0)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()