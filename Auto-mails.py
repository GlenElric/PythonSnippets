import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
sender_email = "***********@********.com"
sender_password = "**************" 

# Email details
subject = "Selection Process for NCC Naval Unit- October 14th, 2024"
body = """Dear [Candidate Name],
Jai Hind!

We are pleased to inform you that you have been shortlisted for the selection process for the Naval NCC SJEC. The selection process will be held on **October 14th, 2024**, commencing at **2:00 PM** and concluding at **5:00 PM**.

The selection process will consist of the following:

**2:00 PM - 3:00 PM:** Written Test
**3:00 PM - 5:00 PM:** Physical Ability Test

Please arrive at NCC room, Opposite PED (AB3 Ground Floor) by **1:45 PM** on the day of the selection process. We advise you to stay hydrated and carry a water bottle.

**Dress Code:** T-shirt (preferably collared) with track pants and sports shoes.

We look forward to meeting you and wish you the best of luck.

Sincerely,
L Cdt.Glen Elric
NCC Naval Unit, SJEC

"""

# List of candidate emails
candidates = [
    "recipient1@gmail.com"
]

# Create a secure connection with the server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, sender_password)

for candidate_email in candidates:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = candidate_email
    msg['Subject'] = subject

    # Replace placeholder with candidate name
    personalized_body = body.replace("[Candidate Name]", candidate_email.split("@")[0])

    # Attach the body to the message
    msg.attach(MIMEText(personalized_body, 'plain'))

    # Send the email
    server.sendmail(sender_email, candidate_email, msg.as_string())

# Close the connection
server.quit()

print("Emails sent successfully!")