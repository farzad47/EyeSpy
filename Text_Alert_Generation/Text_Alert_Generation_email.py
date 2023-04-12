from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

sender_email = "saikrishnakittu0209@gmail.com" # TODO: replace with your email address
receiver_email = ["hanishaasai@gmail.com"] # TODO: replace with your recipients
password = 'orzajesynvflmfcc'  # TODO: replace with your 16-digit-character password 

# assuming these two values are from your analysis
score = 0.86
today_date = '2023-04-04'

# initialise message instance
msg = MIMEMultipart()
msg["Subject"] = "Training Job Notification on {}".format(today_date)
msg["From"] = sender_email
msg['To'] = ", ".join(receiver_email)

## Plain text
text = """\
This line is to demonstrate sending plain text."""

body_text = MIMEText(text, 'plain')  # 
msg.attach(body_text)  # attaching the text body into msg

html = """\
<html>
  <body>
    <p>Hi,<br>
    <br>
    This is to inform the training job has been completed. The AUC for the job on {} is {} <br>
    Thank you. <br>
    </p>
  </body>
</html>
"""
## Image


context = ssl.create_default_context()
# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # check connection
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # check connection
    server.login(sender_email, password)

    # Send email here
    server.sendmail(sender_email, receiver_email, msg.as_string())

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
