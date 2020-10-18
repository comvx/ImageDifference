from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

vs = cv2.VideoCapture("/home/comvx/Downloads/test.mp4")
firstFrame = None
count = 0

while True:
	frame = vs.read()
	frame = frame[1]
	text = "Unoccupied"

	if frame is None:
		break

	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 75, 255, cv2.THRESH_BINARY)[1]

	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < 1000:
		    text = "Occupied"

	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	key = cv2.waitKey(1) & 0xFF


# cleanup the camera and close any open windows
cv2.destroyAllWindows()