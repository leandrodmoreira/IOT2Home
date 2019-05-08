#!/usr/bin/python
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iottohome001@gmail.com","******")
msg = "Hello World!"
server.sendmail("iottohome001@gmail.com","leandrodmoreira@gmail.com",msg)
server.quit()
