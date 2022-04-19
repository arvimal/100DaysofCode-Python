#!/usr/bin/env python3

# smptlib is the module through which
# we can interact with an SMTP server.

# It can be used to authenticate with mail servers,
# send mails, retrieve mails etc..

import smtplib

HOST = "smtp.mail.yahoo.com"
SUBJECT = "Testing smtplib."
TO = "user@gmail.com"
FROM = "user@gmail.com"
PORT = 465
CONTENT = "Hello, how are you today?"

BODY = "\r\n".join((f"From: {FROM}", f"To: {TO}", f"Subject: {SUBJECT}", "", CONTENT))


server = smtplib.SMTP(HOST, PORT)
server.sendmail(FROM, [TO], BODY)
server.quit()
