# Meeting Minutes - 03/21/2023

## Attendees
Alex, Anusha

## Agenda
- Talk about progress this weekend
  - Facial Recognition: Alex
  - Backend: Farzad
  - Frontend: Anusha

## Notes / Comments
- Although this meeting was scheduled for 3/20/23, we moved it back one day because of a scheduling issue.
- Facial Recognition:
  - Coded files using OpenCV for training and testing the facial recognition model
  - File converts frames of live webcam feed into grayscale and compares any detected faces with the faces in Authorized Individuals
  - Added multiple selfie images of myself into a folder named "Alex" in the "Authorized Individuals" directory
  - Model determines which authorized individual trained in the system is closest to the face detected in the live feed
  - Prints the confidence of the prediction of the model to the console
  - Suggestion: We can require the account owner to upload a minimum of 5 or 10 images of each person (but suggest uploading more)
  - Suggestion: Maybe an unauthorized individual is detected if the confidence of the system is lower than a certain percentage. I am unsure about this though and will need to test the system more to see how it may react with this
  - Possibly create subfolder to authorized individuals corresponding to each home which then includes the people folders
  - Create a threshold for prediction confidence
- Backend:
  - We need some sort of backend created so that we can update the code to retrieve testing images from the database.
- Frontend: 
  - Tabs for information About and Services
  - Created a form for the account user when setting up an account
  - Created a tab for a demo
  - Demo is tentatively going to be used to show off the product using the webcam

## Action Items
- To Do:
- Anusha:
  - Email alert generation
  - Login Page/Complete UI
- Sai Krishna:
  - Text message alert generation
- Alex:
  - Do additional testing with facial recognition
- Farzad:
  - Set up backend database (SQL and AWS)

- Farzad and Anusha: Connect the frontend form submission to the backend database


- Next meeting: 03/24/23 (Friday)
