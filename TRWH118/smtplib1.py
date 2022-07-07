import smtplib

main=smtplib.SMTP_SSL('smtp.gmail.com',465)

sender_mail = "saranc1231@gmail.com"
password="pass1231"
receiver_mail ="sccreation11111@gmail.com"

msg='Hello Saran...!'

main.login(sender_mail,password)
main.sendmail(sender_mail,password,receiver_mail,msg)

print("Mail send successfully")
main.quit()