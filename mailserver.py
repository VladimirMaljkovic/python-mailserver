import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import credentials


def send_email(data):
    # Set up the server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = credentials.SMTP_USER
    smtp_password = credentials.SMTP_PASSWORD

    # Create the email(s)

    for receiver_email in credentials.RECEIVER_EMAILS:
        sender_email = smtp_user
        receiver_email = receiver_email
        subject = "Alert triggered"
        body = f"Received data:\n\n{data}"

        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print(f"Email to {receiver_email} sent successfully!")
