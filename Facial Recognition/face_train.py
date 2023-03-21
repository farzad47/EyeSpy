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
features = []
#Array of labels to correlate each image with a person
labels = []

def Scan():

    for person in authorized:
        #Determine the path for each authorized individual
        path = os.path.join(dir_auth, person)
        #Create a label (based on index in folder) for each authorized individual
        label = authorized.index(person)


        for img in os.listdir(path):
            #Determine path for each image in an individual's folder
            img_path = os.path.join(path,img)

            #Read in the image using OpenCV
            img_array = cv.imread(img_path)
            #Convert the image to grayscale
            grayImg = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            #Detect the face(s) in image
            faces_rect = haar.detectMultiScale(grayImg, scaleFactor=1.1, minNeighbors=4)

            #Find the rectangle region containing the face(s)
            for(x,y,w,h) in faces_rect:
                faces_region = grayImg[y:y+h, x:x+w]
                #Add the face/label to the array of faces and array of labels
                features.append(faces_region)
                labels.append(label)


Scan()
print("Scanning complete ----------------------")

#Print the amount of faces and the amount of indexed labels for those faces (should match)
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

#Instantiate the facial recognition
face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Convert features and labels lists to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

#Train the recognizer on the features list and labels list
face_recognizer.train(features,labels)

#Save the trained data 
face_recognizer.save('faces_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)