import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template


new_message = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Michael'
email['to'] = 'antiha8erz@gmail.com'
email['subject'] = 'This is a super secret message!'

email.set_content(new_message.substitute({'name': 'Adrianne'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.login('onelife9788@gmail.com', 'tnsdnjdooaczptfg')
    smtp.send_message(email)
    print('completed!')


