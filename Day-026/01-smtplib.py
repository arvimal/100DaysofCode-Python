#!/usr/bin/env python3

# smptlib is the module through which
# we can interact with an SMTP server.

# It can be used to authenticate with mail servers,
# send mails, retrieve mails etc..

import smtplib

HOST = "smtp.mail.yahoo.com"
SUBJECT = "Testing smtplib."
TO = "arvimal@yahoo.in"
FROM = "arvimal@yahoo.in"
PORT = 465
CONTENT = "Hello, how are you today?"

BODY = "\r\n".join(
    (
        "From: {}".format(FROM),
        "To: {}".format(TO),
        "Subject: {}".format(SUBJECT),
        "",
        CONTENT,
    )
)

server = smtplib.SMTP(HOST, PORT)
server.sendmail(FROM, [TO], BODY)
server.quit()
