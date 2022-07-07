import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='saranc1231@gmail.com',
    to_emails='sccreation11111@gmail.com',
    subject='Sample Mail',
    html_content='<strong>hi...!</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
#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