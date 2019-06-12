import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__)

if __name__ == '__main__':

    tracker_types = ['Boosting', 'MIL', 'KCF', 'TLD','MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)

    else:
        if tracker_type == 'Boosting':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == 'CSRT':
            tracker = cv2.TrackerCSRT_create()

    # Reading the Video File
    video = cv2.VideoCapture("")

    # Exit if video not opened
    if not video.isOpened():
        print "Could not open Video"
        sys.exit()

    # Read the first Frame
    ok, frame = video.read()
    if not ok:
        print "Cannot read video file"
        sys.exit()

    # Define the initial bounding box
    bbox = (287,23,86,320)

    # Uncomment the line below to select a different bbox
    bbox = cv2.selectROI(frame, bbox)

    while True:
        ok, frame = video.read()
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / cv2.getTickCount() - timer

        # Draw a bounding bbox
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1]+bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0))

        else:
            cv2.putText(frame, "Tracking faliure detected")

        # Display FPS on Frame
        cv2.putText(frame, tracker_type + "Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0, 0, 255),2)

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break        
