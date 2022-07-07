import smtplib
from email.mime.text import MIMEText

sender = 'saranc1231@gmail.com'
receivers = ['sccreation11111@gmail.com']

port = 1025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'saranc1231@gmail.com'
msg['To'] = 'sccreation11111@gmail.com'

server=smtplib.SMTP('smtp.gmail.com',587)
server.login('saranc1231@gmail.com', 'bgzkzizwzbgiiylx')
server.sendmail(sender, receivers, msg.as_string())
print("Successfully sent email")