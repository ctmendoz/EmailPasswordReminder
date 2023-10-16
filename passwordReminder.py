#Carlos Mendoza - Password Renewal Reminder
import csv
import getpass
#Don't forget to "pip install schedule" in order to use the schedule module
import schedule
import time
import random
import string
#Don't forget to "pip install secure-smtplib" in order to use the schedule module
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def send_email(email, emailPassword, recipient_emails):
    sender_email = email
    sender_password = emailPassword

    for indiv_recipient_email in recipient_emails:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = indiv_recipient_email
        msg["Subject"] = "Scheduled Email"
        pgen = generate_password()
        message = "This is an experimental scheduled email sent after a minute. Your new generated password is\n" + pgen + ""
        msg.attach(MIMEText(message, "plain"))
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, indiv_recipient_email, msg.as_string())
            server.quit()

def main():
    user_email_input = input("Log into the email you wish to send from\nEmail: ")
    user_password_input = getpass.getpass("Password: ")
    email_list = []
    print("A message regarding a new password will be sent to the following emails every minute (CTRL + C to stop the process): ")

    with open('EmailRecipientList.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        #Read and skip the header row
        headers = next(csvreader)
        for row in csvreader:
            #Process data without headers
            #This will print each row as a list
            print(row)  
            email_list.append(row)

    #Uncomment one and comment the others below in order to change the rate at which emails are sent
	#schedule.every(1).days.do(send_email(user_email_input, user_password_input))
    #schedule.every(1).hours.do(send_email(user_email_input, user_password_input))
    schedule.every(1).minutes.do(send_email(user_email_input, user_password_input, email_list))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

