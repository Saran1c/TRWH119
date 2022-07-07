import smtplib

sender = 'saranc1231@gmail.com'
receivers = ['sccreation11111@gmail.com']

message = 'message'

try:
    smtp_obj = smtplib.SMTP('localhost')
    smtp_obj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")