import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "#Your email"
sender_password = "#Your password"

emails_mapping = {
    "Recipient1": "recipient1@mail.com",
    "Recipient2": "recipient2@mail.com",
}
subject = "Customized subject for each Recipient"
body = """ Salutation {name},
#Email tailored according to your requirement 

"""


# Create a secure connection with the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, sender_password)

for candidate_name, candidate_email in emails_mapping.items():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = subject

    # Attach the body to the message
    personalized_body = body.format(name=candidate_name)
    msg.attach(MIMEText(personalized_body, 'plain'))

    # Send the email
    server.sendmail(sender_email, candidate_email, msg.as_string())

# Close the connection
server.quit()

print("Emails sent successfully!")