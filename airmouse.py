import cvzone
import cv2
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cvzone.HandDetector(detectionCon=0.5, maxHands=1)

flag=True

size=list(pyautogui.size())
sx=size[0]
sy=size[1]
while True:
    # read frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    try:
        #coordinates of hand for mouse
        box=lmList[0][1:]
        x=box[0]
        y=box[1]
        #change according to screen ratio
        #below changes are for 1366x768
        mx=(x-60)*3
        my=(y-100)*2
        if mx>0 and mx<sx and my>0 and my<sy:
            pyautogui.moveTo(1360-mx, my)
            #click if no. of fingers is 0
            if lmList:
                fingers = detector.fingersUp()
                totalFingers = fingers.count(1)
                if totalFingers==0:
                    print('clicked')
                    pyautogui.click(1360-mx, my)
                elif totalFingers==1:
                    print('doubleclicked')
                    pyautogui.doubleClick(1360-mx, my)
        
    except:
        pass
    # Display
    #cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
