# Meeting Minutes - 03/30/2023
## Attendees
Alex, Sai Krishna
## Agenda
- Alex: Model Confidence
- Sai Krishna & Anusha: Alert Generation
- Farzad: Backend Update

## Notes / Comments
- Model Confidence:
  - Through my research, I found that the lower the number for confidence, the better the match (0 is a perfect match)
  - Tested the saved images (of myself) against random images of people online
  - Most images were high (above 100), but some of them were closer to 60 or 70 which is around what it detects when I am on live camera
  - Additionally, some images showed that faces were detected in the background (which is a calibration issue that may need to be changed depending on the image)
  - My only thought on how to improve the real confidence of the model detecting the authorized individual would be to upload more images.
- Alert Generation:
  - GSM module
  - Paid subscription with hardware
  - API
  - Works in other countries but is currently not working in the US
  - Text message generation is more difficult than email generation
  - Can also potentially be used with WhatsApp
  - Sai believes this is the better option and can also be used for the email

## Action Items
- Model Confidence:
  - Potentially use video in database for authorized individual (would include many more frames than just a few pictures)
  - Attempt to increase the number of images of authorized user and see if this improves confidence.
  - Fine-tune the algorithm (training?) in attempt for the facial detection to be more accurate.
- Alert Generation:
  - Sai is going to use the API for both email and text alert generation (update the code within two days)
  - Need the database information to test

- We need an update from Farzad on the backend and the data in the database that we can use for testing

- Next Meeting: Sunday Midday (Determine exact time in WhatsApp with team).
