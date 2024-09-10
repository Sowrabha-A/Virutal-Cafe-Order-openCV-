import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackgraound = cv2.imread('D:\Project Python New\Resources\Background.png')

while True:
    success, img = cap.read()
    #feed on bg
    imgBackgraound[139:139+480, 50:50+640] = img



    #display img
    #cv2.imshow('Image', img)
    cv2.imshow('Background', imgBackgraound)
    cv2.waitKey(1)
