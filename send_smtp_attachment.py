import smtplib
import argparse
import uuid
import time
from email.message import EmailMessage

parser = argparse.ArgumentParser(description="Sends test emails")
parser.add_argument("-u", "--user", help="SMTP username" )
parser.add_argument("-p", "--password", help="SMTP Password")
parser.add_argument("--server", help="hostname for SMTP server")
parser.add_argument("--port", default=587, type=int, help="SMTP server port")
parser.add_argument("--to", default=str(uuid.uuid1()) + "@mailsac.com")
parser.add_argument("--sender", default=str(uuid.uuid1()) + "@mailsac.com")
parser.add_argument("--subject", default="Test Message" + str(time.gmtime()))
args = parser.parse_args()

msg = EmailMessage()
msg.set_content("Email Message Body")
msg['Subject'] = "Test Email" + args.subject
msg['From'] = args.sender
msg['To'] = args.to

server = smtplib.SMTP(args.server, args.port)
server.starttls()
server.login(args.user, args.password)
server.send_message(msg)
server.quit()

print("To: " + args.to + "\r\n" + "From: " + args.sender + "\r\n" + "Subject: "
     + args.subject + "\r\n" + "Inbox: " + "https://mailsac.com/inbox/" +
     args.to)