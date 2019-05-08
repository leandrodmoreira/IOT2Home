#!/usr/bin/python3

# import libraries
from datetime import datetime
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import time

while True:

    # Gravando a data e hora 

    now = datetime.now()

    nameFile = str('image') + now.strftime('%Y%m%d%H%M') + str('.')  + str('jpg')

    # Gerar a imagem...
    print "Gerando o arquivo..."
    print nameFile
    print " "

    os.system('fswebcam -r 1280x720 -S30 --save image%Y%m%d%H%M.jpg')

    # Lendo a temperatura do CPU

    def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        return(res.replace("temp=",""))

    print("getting temperature...")
    cpuTemp = getCPUtemperature()
    print  cpuTemp
    print " "

    # Enviando o E-mail

    fromaddr = "iottohome001@gmail.com"
    toaddr = "leandrodmoreira@gmail.com"
    passwd = "Iot@1982"
 
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "IOT To Home Report"
 
    body = "Hello Leandro! \n This is your IOT To Home Report \n Raspberry Pi current temperature:" + getCPUtemperature()
    print(body)
    msg.attach(MIMEText(body, 'plain'))
    filename = nameFile
    attachment = open("/home/pi/Public/Email/" + nameFile, "rb")
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

    #Sleep
    time.sleep(3600)