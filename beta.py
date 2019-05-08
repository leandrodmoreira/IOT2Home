#!/usr/bin/python3
import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
fromaddr = "iottohome001@gmail.com"
toaddr = "leandrodmoreira@gmail.com"
passwd = "Iot@1982"
 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Raspberry Pi CPU Temperature - Python email"
 
def getCPUtemperature():
   res = os.popen('vcgencmd measure_temp').readline()
   return(res.replace("temp=",""))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, passwd)
print("getting temperature...")
body = "Raspberry Pi current temperature: " + getCPUtemperature()
print(body)
msg.attach(MIMEText(body, 'plain'))
print("sending mail...")
server.sendmail(fromaddr, toaddr, str(msg))
server.quit()
print("mail sent!")
