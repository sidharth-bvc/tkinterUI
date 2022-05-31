import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time

print("Welcome to Email Marketing")
# This can be read from a csv
emailList = [
  'apmanori@gmail.com',
'ssindhumol163@gmail.com',
'Dr.s.akram373@gmail.com',
'ijenwanaluko@gmail.com',
'joannadiazroman28@gmail.com',
'erangahema99@gmail.com',
'Bayarbaatar1211@mail.com', 
'muawia40@gmail.com',
'adityaaman0344@gmail.com',
'shanmadu.silva@gmail.com', 
'liliyamaxima@gmail.com',
'tacteno2@gmail.com',
'keceynoah@gmail.com',
'gonzalesphillip1992@gmail.com',
'gautamaman1149@gmail.com',
'pulasdivina670@gmail.com',
'Massadehmohammad@gmail.com',
'sweetmemory.poem@gmail.com',
'belley_20@yahoo.com',
'lesbiajanet@yahoo.com',
'Hananhomeda111@gmail.com',
'saihamumtaz64@gmail.com',
'esaleonematlhabaphiri@gmail.com',
'Chethana1.shyamal@gmail.com',
'machawesivecindzi@gmail.com',
'Fielamanubay@gmail.com',
'rowellnovida143@gmail.com'
]

def sendMail(fromEmail, toEmail, subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom("siddharth@hindimeinjankari.com")
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
  
  mailserver.ehlo()
  mailserver.login("siddharthsingh@hindimeinjankari.co.in", "siddharthsingh123") 
  
  mailserver.sendmail(fromEmail, toEmail, msg.as_string())
  mailserver.quit()
  
for email in emailList: 
  fromEmail = "siddharth@hindimeinjankari.com"
  subject = "It is a test message. Please ignore"
  message = "This is test email"
  sendMail(fromEmail, email, subject, message)
  print(f"Mail sent to - {email}")
  time.sleep(2)

print("All emails sent successfully")
