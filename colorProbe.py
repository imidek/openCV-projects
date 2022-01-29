import cv2
import numpy as np
def klik(event, x, y, ad, da):
    global evt
    global xPos
    global yPos
    yPos = y
    xPos = x
    evt = event
    event = 0

width = 640
height = 480 
frameW = 350
frameH = 350
yPos = 0
xPos = 0
evt = 0
pr = 0
ipt = 0

cam = cv2.VideoCapture(0)
cam.set(3,width)
cam.set(4,height)
cv2.namedWindow('img')
cv2.setMouseCallback('img', klik)

while ipt==0:
    choice = int(input('How many probes would you take? (max 5): '))
    if choice > 0 and choice <=5:
        ipt = 1
    if choice > 5:
        print('Too much of a good thing. Max is 5 probes. ')
        choice = 5
        ipt = 1
    else:
        print('Try again. Choose wisely!')
print('You have ' + str(choice) + ' probes. Hover over image and click LMB.')
pointsHSV = []
pointsBGR = []
trig = 1

while True:
    zzz, img = cam.read()
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow('img', img)
    cv2.moveWindow('img', 0, 0)

    if evt == cv2.EVENT_LBUTTONDOWN:
        z = (yPos,xPos)
        a = hsvImg[z]
        b = img[z]
        print(a)
        #print(b)
        pointsHSV.append(a)
        pointsBGR.append(b)
        evt = 0
           
    if len(pointsHSV)==choice and trig == 1:
        pr = 1
        print('')
        trig = 0
        for point in range (len(pointsHSV)):
            print('Point',point+1,'in HSV is', pointsHSV[point],'and in BGR is',pointsBGR[point])
    
    if pr == 1:
        pr = 0    
        for i in range (len(pointsHSV)):
            j = np.zeros([frameH,frameW,3],np.uint8)
            j[:] = pointsBGR[i]
            name = 'Probe ' + str(i+1) + ', HSV value ' + str(pointsHSV[i])
            cv2.imshow(name,j)
            cv2.moveWindow(name,int(i+i*frameW), height+10)
            #print(pointsHSV[i])
        print('\nType "q" to exit the program. Thank You.')
    
    
        

    

    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break




    

    
        