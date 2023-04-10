import os
import cv2 as cv
import numpy as np
import urllib
import mysql.connector as sql
from Final_Text_Alert_Generation import *

#Make connection to the SQL Host
db = sql.connect(
    host="database-eyespy.cyvbyvilxbbf.us-east-2.rds.amazonaws.com",
    user="admin",
    password="Master123",
    database="sys"
)

#Object that allows us to write SQL statements for database
cursor = db.cursor(buffered=True)

#Specifying CameraID - This would be dynamic in real-world model
cameraID = 1

#Execute a query to find the current camera ID
cursor.execute("SELECT * FROM customer_cam_mapping WHERE CAM_ID LIKE " + str(cameraID))
qResults = cursor.fetchall()

customerID = qResults[0][0]

#Execute a query to find the owner of the camera
cursor.execute("SELECT * FROM authorized_customer_mapping WHERE CUSTOMER_ID LIKE " +  str(customerID))
qResults = cursor.fetchall()

#List of authorized individuals
authorized = []
authorizedID = []

#Creating list of authorized ID's
for row in qResults:
    authorizedID.append(row[2])

#Start of next query
detailQuery = "SELECT * FROM person_detail WHERE "

#Include only each authorized ID in this query
for i in range(len(authorizedID)):
    detailQuery += ("PERSON_ID LIKE " + str(authorizedID[i]))
    if i < len(authorizedID) - 1:
        detailQuery += " OR "

#Execute query to find each authorized individual for the given camera/address
cursor.execute(detailQuery)
qResults = cursor.fetchall()

#Print the results in console
for row in qResults:
    authorized.append(row[1])

#Declaring classifier as haar cascade face detection
haar = cv.CascadeClassifier('haar_face.xml')

#Print list of authorized individuals
print(authorized)

#Image arrays of faces
features = []
#Array of labels to correlate each image with a person
labels = []

def Scan():

    for person in qResults:

        exists = os.path.exists("Authorized_Individuals")
        if not exists:
            os.makedirs("Authorized_Individuals")

        #Create a label (based on index in folder) for each authorized individual
        label = person[0]
        name = person[1]

        exists = os.path.exists("Authorized_Individuals\\\\" + name)
        if not exists:
            os.makedirs("Authorized_Individuals\\\\" + name)

        personalImages = person[5].split(",")
        
        print(personalImages)

        for url in range(len(personalImages)):

            imgPath = personalImages[url].split("/")[-1]
            localPath = "Authorized_Individuals\\\\" + name + "\\\\" + imgPath

            exists = os.path.exists(localPath)
            if not exists:
                urllib.request.urlretrieve(personalImages[url], localPath)

            #Read in the image using OpenCV
            imgArray = cv.imread(localPath)
            #Convert the image to grayscale
            grayImg = cv.cvtColor(imgArray, cv.COLOR_BGR2GRAY)
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