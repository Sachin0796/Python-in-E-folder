import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'msgtosachin@gmail.com'
sender_password = 'fxxfsuqydnvosvgr'
receiver_email = 'msgtosachin@gmail.com'

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = sender_email
message['Subject'] = 'Hello from Python'
message['CC'] = sender_email
message['BCC'] = sender_email

body = 'Email body.'
message.attach(MIMEText(body, 'plain'))

# Attach the file
# filename = 'C://Users//msgto//Downloads//Investment.txt'  # Replace with the path to your file
# attachment = open(filename, 'rb')

# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', 'attachment', filename=filename)
# message.attach(part)

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Send the email
server.sendmail('sender_email', receiver_email, message.as_string())

# Disconnect from the server
server.quit()

print('Email sent successfully!')