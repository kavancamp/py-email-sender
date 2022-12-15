from email.message import EmailMessage
from pword import password
import certifi
import ssl
import smtplib


email_sender = 'kvancamp27@gmail.com'
email_password = password
email_receiver = 'lakahe1247@dni8.com'

subject = "Don't forget to subscribe"
body = """
When you watch a video, please subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


#context = ssl.create_default_context()
context=ssl.create_default_context(cafile=certifi.where())

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())

