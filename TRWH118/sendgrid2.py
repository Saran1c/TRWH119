import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='saranc1231@gmail.com',
    to_emails='sccreation11111@gmail.com',
    subject='Sending Mail',
    html_content='<strong>Hello..Saran</strong>')

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)