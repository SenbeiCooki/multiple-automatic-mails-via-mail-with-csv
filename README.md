# Multiple Automatic Mails via CSV
This Python script automates the process of sending emails to multiple recipients using data from a CSV file. The script allows you to customize each email based on the data provided in the CSV, and it includes the option to attach a PDF file to each email.

Features
Reads contact information (email addresses and names) from a CSV file.
Sends personalized emails to each recipient based on the provided name.
Allows attachment of a PDF file to each email.
Configurable SMTP settings to send emails through your mail provider.

Prerequisites:
Python 3.x
Required Python libraries:
pandas
smtplib
email.mime


## How to Use:
1. CSV File Format
The script reads a CSV file to retrieve email addresses and recipient names. The CSV should have the following format:

1. line: email,name
2. line: example1@gmail.com	Genossenschaft A
3. line: example2@gmail.com	Genossenschaft B


2. Script Configuration
Before running the script, you need to configure the following variables in the script:

Sender Email: Replace 'YOUR_MAIL' with your email address in the msg['From'] field.
SMTP Login Credentials: Replace 'p.wiesemann@hotmail.de' and 'XXXXXXX' with your email and password in the server.login() function.
Note: If you're using an email provider like Gmail, you may need to generate an App Password or use an OAuth-based login for security.
