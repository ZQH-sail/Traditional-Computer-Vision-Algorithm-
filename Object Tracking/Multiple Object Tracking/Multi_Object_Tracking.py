import numpy as np
import cv2
import imutils
import time
from imutils.video import VideoStream

## Creating a multitracker object
trackers = cv2.MultiTracker_create()

## Reading the video file into the code
video = cv2.VideoCapture('../data/traffic.mp4')

# Initializing the boxes
#boxes = None

# Variable for counting frame number
i = 0
# Loop over all the frames
while True:

    # Grab the current frame
    success,frame = video.read()
    #print(success)
    i = i+1
    # Checking whether frames are left or not
    if not success:
        break

    # Lesser size lesser information hence resizing helps
    #frame = imutils.resize(frame, width = 700)

    #if boxes is not None:
    # Generate the updates from tracker if the boxes are present
    success, boxes = trackers.update(frame)
    #print(success)

    # For box in boxes.
    for box in boxes:
        (x,y,w,h) = [int(v) for v in box]
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,255) ,2)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(25)

    ## If you press key s, you will be given an option to select a bounding box.
    if key == ord("s"):
        ## Select the desried bounding boxes.
        box = cv2.selectROI("Frame", frame, fromCenter = False, showCrosshair = False)
        # boxes.append(box)
        ## Create a new object tracker to handle this particular tracking task
        tracker = cv2.TrackerCSRT_create()
        trackers.add(tracker,frame,box)

    elif key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
