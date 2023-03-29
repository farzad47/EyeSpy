import os
import cv2 as cv
import numpy as np



#List of authorized individuals
authorized = []

#Declaring classifier as haar cascade face detection
haar = cv.CascadeClassifier('haar_face.xml')

#Directory holding authorized individuals
dir_auth = "Auth_Individuals"

#Get List of authorized individuals (as their directories)
for i in os.listdir(dir_auth):
    authorized.append(i)
#Print list of authorized individuals
print(authorized)

#Image arrays of faces
features = np.load('features.npy', allow_pickle=True)
#Array of labels to correlate each image with a person
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('faces_trained.yml')

def TestAccuracy():
    #Directory holding authorized individuals
    dir_test = "Test_Accuracy"
    for i in os.listdir(dir_test):
        test_image_path = dir_test + '\\' + i
        
        print(test_image_path)

        test_image = cv.imread(test_image_path)

        grayTestImg = cv.cvtColor(test_image, cv.COLOR_BGR2GRAY)

        #Coordinates of face in the image
        faces_rect = haar.detectMultiScale(grayTestImg, scaleFactor=1.1, minNeighbors=5)

        #Draw square locations where faces are found within the video
        for (x,y,w,h) in faces_rect:
            faces_region = grayTestImg[y:y+h,x:x+h]
            cv.rectangle(grayTestImg, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        label, confidence = face_recognizer.predict(faces_region)
        print(f'Label = {authorized[label]} with a confidence of {confidence}')

        cv.putText(grayTestImg, str(authorized[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

        #Display image with rectangles
        #cv.imshow(i, grayTestImg)

def LiveVideo():
    #Video Input Capture [0 corresponds to laptop webcam]
    cpt = cv.VideoCapture(0)

    while True:
        # Read each frame of the video
        isTrue, frame = cpt.read()

        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #Coordinates of face in the video
        faces_rect = haar.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=5)

        #Draw square locations where faces are found within the video
        for (x,y,w,h) in faces_rect:
            faces_region = grayFrame[y:y+h,x:x+h]
            cv.rectangle(grayFrame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        label, confidence = face_recognizer.predict(faces_region)
        print(f'Label = {authorized[label]} with a confidence of {confidence}')

        cv.putText(grayFrame, str(authorized[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

        #Display video with rectangles
        cv.imshow('Video', grayFrame)

        #Stop reading if 'D' key is pressed
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    #Stop capturing and remove video display window(s)
    capture.release()
    cv.destroyAllWindows()

#TestAccuracy()
LiveVideo()

cv.waitKey(0)
