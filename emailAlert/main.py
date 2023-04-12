import smtplib

gmail_user = 'eyespycustomercare6@gmail.com'
gmail_password = 'cpqvekfvqfzlrtoo'


sent_from = gmail_user
to = ['anusha536655@gmail.com']
subject = 'ALERT - Security cam'
body = 'Some unauthorized person tried to enter your house. Hope everything is fine.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)