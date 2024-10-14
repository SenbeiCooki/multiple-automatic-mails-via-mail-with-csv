import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Load CSV file
data = pd.read_csv('C:\\PATH\\CSV.csv')

# Function to send emails
def send_email(to_address, name):
    # Customize email content
    subject = "Application for an apartment"
    body = f"""Dear members of the {name} cooperative,

My name is XXX, and I am currently looking for an apartment. Someone told me about your {name} cooperative, and I am very interested in becoming a member as well as finding an apartment with the goal of continuing the cooperative spirit. Unfortunately, I couldn't find any information about available apartments on your website, so I am writing you this email in the hope that you could put me on a waiting list. Attached you will find my completed application form. I would be very happy to receive a reply.

Best regards,

XXX
"""
    
    msg = MIMEMultipart()
    msg['From'] = 'YOUR_MAIL'
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

   # Add attachment
    with open('PDF_NAME.pdf', 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name='PDF_NAME.pdf')
    part['Content-Disposition'] = 'attachment; filename="PDF_NAME.pdf"'
    msg.attach(part)

    # Set up SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.office365.com', 587) #add smtp of your email this is hotmail
        server.starttls()
        server.login('YOUR_MAIL', 'EMAIL_PASSWORD')
        server.send_message(msg)
        server.quit()
        print(f'Email sent successfully.')
    except Exception as e:
        print(f'Error sending email: {e}')

# Send emails to all cooperatives
for index, row in data.iterrows():
    send_email(row['email'], row['name'])
