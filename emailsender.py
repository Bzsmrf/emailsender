# bwnh lyvx rwlx mxme
from email.message import EmailMessage
# from app2 import pwrd
import ssl
import smtplib

email_sender = 'dozerzzzz1234@gmail.com'
email_password = 'bwnh lyvx rwlx mxme'

email_receiver = 'bakom82115@vpsrec.com'

subject = "Donot forget to Subscribe"
body = """
when you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


