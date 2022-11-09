"""
This is a class to send the emails to the receivers
"""
import smtplib
from email.message import EmailMessage
import time

class email:
    def __int__(self):
        pass
    def send_message(self, mail_to, link):
        self.server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        self.server.starttls()
        self.server.login('mohamad.aminalhajj@outlook.com', 'Mohamad_123')
        self.msg = EmailMessage()
        self.msg.set_content(f"This is the link: \n{link} \n")
        self.msg['Subject'] = f'A new Car has arrived !'
        self.msg['From'] = 'mohamad.aminalhajj@outlook.com'
        self.msg['To'] = mail_to
        self.server.send_message(self.msg)
        self.server.quit()
