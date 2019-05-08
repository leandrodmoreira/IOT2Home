#!/usr/bin/python3
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from picamera import PiCamera
import os


 
fromaddr = "iottohome001@gmail.com"
toaddr = "leandrodmoreira@gmail.com"
passwd = "********"
 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hello from Raspberry Pi - Python email"
 
body = "Hello World!"
msg.attach(MIMEText(body, 'plain'))
filename = "image.jpg"
attachment = open("/home/pi/Public/Email/image.jpg", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
 
print("sending mail...")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, passwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("email sent!")
