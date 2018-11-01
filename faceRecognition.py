import cv2
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
#second_camera = cv2.VideoCapture(1)

while True:

    # Capture frame-by-frame
    retval, frame = video_capture.read()
    #ret, frame2 = second_camera.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Detect features specified in Haar Cascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )

    #faces = faceCascade.detectMultiScale(
    #    gray2,
    #    scaleFactor=1.1,
    #    minNeighbors=5,
    #    minSize=(35, 35)
    #)

    # Draw a rectangle around recognized faces 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255, 255), 2)
        #cv2.rectangle(frame2, (x, y), (x+w, y+h), (0,0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    #cv2.imshow('Video note', frame2)

    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == ord('q'):
       sys.exit() 
