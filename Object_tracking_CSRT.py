from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import numpy as np
import cv2

# Using the CSRT Tracker
tracker = cv2.TrackerCSRT_create()
tracker_type = 'CSRT'

# Initializing the Bounding box
initBB = None

# Reading the video from a pre-known path.
video = cv2.VideoCapture('car_moving.mp4')

# Initializing the FPS throughput
fps = None

# Looping over the frames
while True:

    ## Grab the current frame.
    ok,frame = video.read()
    #frame = np.array(frame)

    ## Checking whether the end is reached or not.
    if frame is None:
        break

    ## Resizing the input in order to fasten the process of object
    ## tracking
    frame = imutils.resize(np.array(frame))
    #high,width = frame.shape()

    ## Checking whether currently something is being tracked or not
    if initBB is not None:
        # Grab the new bounding box coordinates of the object
        # using the tracker_type
        (success, box) = tracker.update(frame)

        # Check to see if the tracking was a success
        if success:
            (x,y,w,h) = [int(v) for v in box]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        else:
            cv2.putText(frame, "Tracking faliure detected", (120,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Updating the FPS Counter
        fps.update()
        fps.stop()

        # Initialize the set of information we'll be displaying on
        # the frames
        info = [("tracker", tracker_type), ("Success", "Yes" if success else 'no'),
        ("FPS", "{:.2F}".format(fps.fps()))]
        #
        ## Loop over the info tuples and draw them on our frames
        for (i,(k,v)) in enumerate(info):
            text = "{}:{}".format(k,v)
            cv2.putText(frame,text,(10,h - ((i*20)+20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)

    # Show the output frame
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(10)
    #print(key)
    #print(ord("s"))
    # if the 'b' key is selected, we are going to "select a bounding box to track"
    if key == ord("s"):
        # Select the bounding box of the object we want to TrackerTLD_create
        initBB = cv2.selectROI("Frame", frame, fromCenter = False, showCrosshair = True)
        tracker = cv2.TrackerCSRT_create()
        # initialize the tracker with a particular bounding box
        tracker.init(frame, initBB)
        fps = FPS().start()

    elif key == ord("q"):
        break

# if done
video.release()
cv2.destroyAllWindows()
