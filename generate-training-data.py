import cv2
import os

cap = cv2.VideoCapture(0)


def DataCapture(var):
    count = 0
    root_path = r'C:\\Users\gs199\PycharmProjects\RockPaperScissor'
    path=os.path.join(root_path,var)
    while (cap.isOpened()):
        rep, frame = cap.read()

        if rep == True:
            font = cv2.FONT_HERSHEY_PLAIN
            frame = cv2.rectangle(frame, (100, 100), (400, 400), (255, 0, 0), 5)
            frame = cv2.putText(frame, "count=" + str(count / 5), (300, 420), font, 1, (0, 0, 255), 2)

            if count % 5 == 0:
                cv2.imwrite(os.path.join(path, var + str(count / 5) + '.jpg'), frame[100:400, 100:400])
                print('Number of pictures captured: {}'.format(count / 5))

            count = count + 1

        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


gesture = input('Input the gesture you want to capture')
DataCapture(gesture)
##You can change 'scissor'---> to anything(Rock,paper,scissor) accordingly.
