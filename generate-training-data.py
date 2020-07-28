import os
import cv2

cap = cv2.VideoCapture(0)
count = 0
while (cap.isOpened()):
    rep, frame = cap.read()

    if rep == True:

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #out.write(frame)
        font = cv2.FONT_HERSHEY_PLAIN
        frame = cv2.rectangle(frame, (100,100), (400,400),(255,0,0), 5)
        frame = cv2.putText(frame, "count="+str(count/5), (300, 420), font,1 , (255, 0, 0), 3)
        if count%5 == 0:
            cv2.imwrite('scissor' + str(count/5) + '.jpg', frame[100:400,100:400])
            print('Number of pictures captured: {}' .format(count/5))
        count+= 1

        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

##You can change 'scissor'---> to anything(Rock,paper,scissor) accordingly.
