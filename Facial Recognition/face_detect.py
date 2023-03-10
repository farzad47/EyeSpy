import cv2 as cv

#Video Input Capture [0 corresponds to laptop webcam]
cpt = cv.VideoCapture(0)

while True:
    # Read each frame of the video
    isTrue, frame = cpt.read()

    #Declaring classifier as haar cascade face detection
    haar = cv.CascadeClassifier('haar_face.xml')

    #Coordinates of face in the video
    faces_rect = haar.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    #Draw square locations where faces are found within the video
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    #Display video with rectangles
    cv.imshow('Video', frame)

    #Stop reading if 'D' key is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#Stop capturing and remove video display window(s)
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
