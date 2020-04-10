import getpass
import poplib
import argparse

parser = argparse.ArgumentParser(description="check pop3 mailbox")
parser.add_argument("-u", "--user", help="pop3 username" )
parser.add_argument("-p", "--password", help="pop3 Password")
parser.add_argument("--server", help="hostname for pop3 server")
parser.add_argument("--port", default=110, type=int, help="pop3 server port")
args = parser.parse_args()

M = poplib.POP3(args.server, port=args.port)
M.user(args.user)
M.pass_(args.password)
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)