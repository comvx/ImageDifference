import cv2
import numpy as np


images = []

cap = cv2.VideoCapture("./out.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("./out.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
while True:
    boolen, frame = cap.read() # get the frame
    if flag:
        np_frame = cv2.imread('video', frame)
        images.append(np_frame)

        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    else:
        break

all_frames = np.array(images)