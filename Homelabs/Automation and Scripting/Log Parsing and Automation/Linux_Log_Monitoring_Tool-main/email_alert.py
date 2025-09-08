import smtplib
from email.mime.text import MIMEText

def send_email_alert(anomalies):
    sender_email = "youremailaddress"
    receiver_email = "receiveremailaddress"
    subject = "Fraudulent Activity Detected"
    body = anomalies.to_string()

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "yourapppassword")
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Send alert if anomalous
if not anomalies.empty:
    send_email_alert(anomalies)
