#  import random

# otp= random.randint(1000,9999)
# print("your otp is :",otp)

import smtplib
import random

# Replace these with your email configuration
smtp_server = 'smtp.gmail.com'
sender_email = 'prajkumar1200@gmail.com'
sender_password = 'Pandey@1200'
recipient_email = 'rounakpandey1200@gmail.com'

# Generate a random 4-digit OTP
otp = random.randint(1000, 9999)

# Compose the email message
subject = 'Your OTP'
body = f'Your OTP is: {otp}'
message = f'Subject: {subject}\n\n{body}'

# Send the email
try:
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message)
    print('Email sent successfully.')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()
