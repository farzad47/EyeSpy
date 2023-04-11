import os
import cv2 as cv
import numpy as np
import mysql.connector as sql
from Final_Text_Alert_Generation import *
import face_train
from flask import Flask, render_template, render_template_string, Response

#Run training prior to recognizing
face_train.__name__

#Instantiate Flask application
app = Flask(__name__)

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

#Get the details for the customer (account owner)
cursor.execute("SELECT * FROM person_detail WHERE PERSON_ID LIKE " + str(customerID))
customerResult = cursor.fetchall()

#Retrieving customer information for alert generation
customerPhone = customerResult[0][3]
customerEmail = customerResult[0][2]
customerCarrier = customerResult[0][6]

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

#Image arrays of faces
features = np.load('features.npy', allow_pickle=True)
#Array of labels to correlate each image with a person
labels = np.load('labels.npy', allow_pickle=True)

#Instantiate a recognizer using OpenCV
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('faces_trained.yml')

@app.route('/')
def index():
    """Video streaming"""
    #return render_template('index.html')
    return render_template_string('''<html>
<head>
    <title>Video Streaming </title>
</head>
<body>
    <div>
        <h1>Image</h1>
        <img id="img" src="{{ url_for('video_feed') }}">
    </div>
    <div>
        <h1>Canvas</h1>
        <canvas id="canvas" width="640px" height="480px"></canvas>
    </div>

<script >
    var ctx = document.getElementById("canvas").getContext('2d');
    var img = new Image();
    img.src = "{{ url_for('video_feed') }}";

    // need only for static image
    //img.onload = function(){   
    //    ctx.drawImage(img, 0, 0);
    //};

    // need only for animated image
    function refreshCanvas(){
        ctx.drawImage(img, 0, 0);
    };
    window.setInterval("refreshCanvas()", 50);

</script>

</body>
</html>''')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(LiveVideo(),
                mimetype='multipart/x-mixed-replace; boundary=frame')

def LiveVideo():
    print("Facial Recognition started ----------------------")
    
    #Video Input Capture [0 corresponds to laptop webcam]
    cpt = cv.VideoCapture(0)

    #Variables for alerts
    queryInsert = []
    emailSent = False

    while True:
        # Read each frame of the video
        isTrue, frame = cpt.read()

        #Convert the frames to grayscale
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #Coordinates of face in the video
        faces_rect = haar.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=5)

        #Draw square locations where faces are found within the video
        for (x,y,w,h) in faces_rect:
            faces_region = grayFrame[y:y+h,x:x+h]
            cv.rectangle(grayFrame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        #Predict confidence for any face detected
        if(len(faces_rect) != 0):
            label, confidence = face_recognizer.predict(faces_region)
            authorization = "Authorized"

            #Send alert if unauthorized individual is detected
            if(confidence > 100 and not emailSent):
                authorization = "Unauthorized"
                sendEmail(customerPhone, customerCarrier, customerEmail)
                emailSent = True
                
                #Archive record of person detected
                if queryInsert.count(details[0][0]) < 1:
                    cursor.execute("INSERT INTO history_all (personName, AlertSent, cust_id, authorized_status, entered_person_cust_id) VALUES ('UNKNOWN','Yes',"+ str(customerID) +",'UNAUTHORIZED','0')")
                    db.commit()
                    queryInsert.append(0)

            #Determine the name of the authorized individual
            else:
                cursor.execute("SELECT * FROM person_detail WHERE PERSON_ID LIKE " + str(label))
                details = cursor.fetchall()
                authorization = details[0][1]
                
                #Archive record of person detected
                if queryInsert.count(details[0][0]) < 1:
                    cursor.execute("INSERT INTO history_all (personName, AlertSent, cust_id, authorized_status, entered_person_cust_id) VALUES ('"+ str(details[0][1]) +"','No','"+ str(customerID) +"','AUTHORIZED','"+ str(details[0][0]) +"')")
                    db.commit()
                    queryInsert.append(details[0][0])

            #Display Authorization level of each person in frame
            for (x,y,w,h) in faces_rect:
                cv.putText(grayFrame, authorization, (x,y-5), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)

            #Display video with rectangles
            cv.imwrite('Screenshot.jpg', grayFrame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + open('Screenshot.jpg', 'rb').read() + b'\r\n')

        #Stop reading if 'D' key is pressed
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    #Stop capturing and remove video display window(s)
    cpt.release()
    cv.destroyAllWindows()

#Run the Flask application
app.run()

cv.waitKey(0)
