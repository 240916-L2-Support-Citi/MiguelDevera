import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# stores credential constants
import Credentials
from GenerateMessage import generate_message

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = Credentials.SENDER
receiver_email = Credentials.RECEIVER
password = Credentials.PASSWORD_E

def send_test_email(num_fatals, num_errors):
    subject = 'Project 1 ALERT SYSTEM (SIMULATION)'
    temp_string = "Hello, this is an email regarding P1. This was a simulation, if you see this in the future don't worry about it.\n"
    temp_string += generate_message(num_fatals,num_errors) #important
    body = temp_string

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(msg.get('From'),msg["To"],msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if server:
            server.quit()  # Close the connection