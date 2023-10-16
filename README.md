<b>I. SUMMARY:</b>
- This program allows the user to sign into their email account and send an automated email to a list of email addresses that can be edited in the EmailRecipientList.csv file.
- The automated email reminds the recipients to change their password for security purposes and recommends a long randomly generated password that is difficult to guess. This email is continuously sent over a specific period of time (days, hours, minutes, etc.) which can be adjusted in lines 54-56 in passwordReminder.py. However, each email sent is unique as it sends a different password each time.

<b>II. HOW TO RUN:</b>
- In order to run this program, I had to use a Python IDE (PyCharm) as certain modules like schedule and getpass were unable to be found when running the program through a terminal.
- Start a new project in the IDE using everything in this repository.
- Include any necessary modules with the project.
- Edit the "EmailRecipientList.csv" file to include any email addresses you wish to send the automated password reminder messages to.
  - Ensure that the email addresses follow the correct format.
- Edit line 54-56 in the passwordReminder.py file to specify how long the wait time should be between emails.
- Run the Python file
