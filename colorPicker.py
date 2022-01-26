import cv2
import numpy as np

def klik(event,xpos,ypos,pa,fa):
    global evt
    global xval
    global yval
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(event)
        evt = event
        xval = xpos
        yval = ypos
    if event == cv2.EVENT_RBUTTONUP:
        evt = event
        print(event)
        
evt=0
xval=0
yval=0


fWidth = 640
fHeight = 480
cam = cv2.VideoCapture(0)
cam.set(3,fWidth)
cam.set(4,fHeight)
cam.set(10,150)
cv2.namedWindow('img')
cv2.setMouseCallback('img',klik)


while True:
    sukces, img = cam.read()
    z = np.zeros([250,250,3],np.uint8)
    clr=img[yval,xval]
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    zhsv = hsv[yval,xval]

    if evt == 1:
        z[:,:] = clr        
        print('In BGR color is:',clr)
        print('In HSV color is:',zhsv ,'\n')
        cv2.imshow('z',z)
        cv2.moveWindow('z',fWidth,0)
        evt=0
    if evt == 5:
        print('bye bye!')
        cv2.destroyWindow('z')
        evt=0
    
    cv2.imshow('img',img)
    cv2.moveWindow('img',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break