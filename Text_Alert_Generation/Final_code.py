from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "spidermanofspider@gmail.com"
PASSWORD = "ixuqbmljbxgvzcig"

def sendEmail(phoneNumber, carrier, email):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = EMAIL # TODO: replace with your email address
    receiver_email = [email] # TODO: replace with your recipients
    password = PASSWORD  # TODO: replace with your 16-digit-character password 
    recipient = "+1" + phoneNumber + CARRIERS[carrier]
    print(recipient)
    
     #Una
    msg = MIMEMultipart()
    msg["Subject"] = "UnAuthorized Person Recognized"
    msg["From"] = sender_email
    msg['To'] = ", ".join(receiver_email)

    ## Plain text
    text = MIMEMultipart()
    text["Subject"]="ALERT!"
    text["From"]= sender_email
    text['To']=", ".join(receiver_email)
    body="Eyespy wants you to take some action  "

    body_text = MIMEText(body, 'plain')  # 
    msg.attach(body_text)  # attaching the text body into msg

    text.attach(body_text)

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
        server.sendmail(sender_email, recipient,text.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()