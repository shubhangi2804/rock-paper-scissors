import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model
import random

# custom pre-process techniques
# import this incase you want to resume the pre-processing techniques
# for the model creation and model predection while playing
# import preprocess

# DO NOT MODIFY THIS
REV_CLASS_MAP = {
    0: "empty",
    1: "rock",
    2: "paper",
    3: "scissors"
}

# DO NOT MODIFY THIS
def mapper(value):
    return REV_CLASS_MAP[value]


def winner(move_by_user, move_by_cmp):

    if move_by_cmp==move_by_user:
        print('Its a tie')

    if move_by_cmp== 'rock':
        if move_by_user=='paper' :
            print('User wins')

    if move_by_cmp=='paper':
        if move_by_user=='scissors' :
            print('User wins')

    if move_by_cmp== 'paper':
        if move_by_user=='rock' :
            print('Computer wins')

    if move_by_cmp=='scissors':
        if move_by_user =='rock':
            print('User wins')

    if move_by_cmp =='scissors':
        if move_by_user == 'paper':
            print('Computer wins')

    if move_by_cmp =='rock':
        if move_by_user == 'scissors' :
            print('User wins')

    if move_by_user=='empty':
        print('Place your hand gesture correcty!')



def main():

    model = load_model("rock-paper-scissors-model.h5")
    cap= cv2.VideoCapture(0)
    c=0

    while(cap.isOpened()):
        rep, frame = cap.read()
        count=0

        if (rep==True):
            font = cv2.FONT_HERSHEY_PLAIN
            frame = cv2.rectangle(frame, (100, 100), (400, 400), (255, 0, 0), 5)
            frame = cv2.putText(frame, "Press 'c' to capture Image " , (95, 95), font, 1, (0, 0, 255), 2)
            frame = cv2.putText(frame, "Captured Images" + str(c), (300, 420), font, 1, (0, 0, 255), 2)
            roi= frame[100:400, 100:400]
            k = cv2.waitKey(1) & 0xFF
            if k== ord('c'):
                cv2.imwrite('CapturedGesture.jpg',roi)
                c=c+1

        cv2.imshow('Capture Gesture',frame)
        if c==2:                        # Your second hand gesture will be considered as final image.   
            break
    cap.release()
    cv2.destroyAllWindows()

    img = cv2.imread('CapturedGesture.jpg',1)
    img = preprocess(img)
    pred = model.predict(np.array([img]))
    move_made_by_you = mapper(np.argmax(pred[0]))

    choices=['paper', 'rock','scissors']
    move_made_by_cmp = random.choice(choices)
    print('Move made by you: {}'.format(move_made_by_you))
    print('Move made by Computer: {}'.format(move_made_by_cmp))
    winner(move_made_by_you, move_made_by_cmp)

main()
