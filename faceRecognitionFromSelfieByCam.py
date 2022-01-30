import cv2
import face_recognition as fr
font = cv2.FONT_HERSHEY_SIMPLEX
red = (0,0,255)
green = (0,255,0) 

cam = cv2.VideoCapture(0)
#selfie = fr.load_image_file('Put here path of your selfie')
selfie = fr.load_image_file('C:/Users/kot/Documents/Python/faceReco/known/wojtekSelfie.jpg.jpg')
selfieLoc = fr.face_locations(selfie)[0]
selfieEncode = fr.face_encodings(selfie)[0]
knownEncodings = [selfieEncode]
names = ['Type in your name']


while True:
    zzz, img = cam.read()
    facesLoc = fr.face_locations(img)
    facesEncode = fr.face_encodings(img, facesLoc)
    if len(facesLoc) > 0:
        for face,code in zip(facesLoc, facesEncode):
            top,right,bottom,left = face
            x = (left, top)
            y = (right, bottom)
            match = fr.compare_faces(knownEncodings,code)
            if True in match:
                matchIndex = match.index(True)
                cv2.rectangle(img, x, y, green, 2)
                cv2.putText(img, names[matchIndex],x,font,1,green,2)
            else:
                cv2.rectangle(img, x, y, red, 2)
                cv2.putText(img, '???',x,font,1,red,2)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()