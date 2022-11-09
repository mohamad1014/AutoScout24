"""
This is to combine all the functionalities and send mails out when needed
"""

from send_mail import email
import time
start = time.time()
mail_setup = email()
mail_setup.send_message(mail_to=["mo7amad.al.7ajj@gmail.com", "mohamad.aminalhajj4@outlook.com"], link="LL.com")
print(f"Time taken to set and send the emails {time.time()-start} sec")
