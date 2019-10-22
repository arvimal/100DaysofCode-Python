#!/usr/bin/env python3

# Example taken from PyMoTW3,
# only for the purpose of understanding
# and studying the module.

"""
MIME = Multipurpose Internet Mail Extensions
From `https://en.wikipedia.org/wiki/MIME`

Multipurpose Internet Mail Extensions (MIME) is an Internet standard that \
extends the format of email to support:

    Text in character sets other than ASCII
    Non-text attachments: audio, video, images, application programs etc.
    Message bodies with multiple parts
    Header information in non-ASCII character sets
"""

# Using `smtplib` to connect to the Mail server, increase debug level,
# and send the mail.
import smtplib

# Using the utils function in the `email` module, for setting the message,
# setting the To, From etc.
import email.utils

# Using `MIMETest` to convert the text to MIME format.
from email.mime.text import MIMEText

# The messages to be send, formatted as proper text MIME format
message = MIMEText("Hello, How are you today?")
message["To"] = email.utils.formataddr(("Recipient", "arvimal@yahoo.in"))
message["From"] = email.utils.formataddr(("Author", "arvimal@yahoo.in"))
message["Subject"] = "Test mail send using smtplib"

# Connect to an SMTP server
# smtplib.SMTP() takes the hostname as the output of `socket.getfqdn()`
# and the port to be what's set for `smtplib.SMTP_PORT`
# This can be overridden, as we're doing below.
mail_server = smtplib.SMTP("smtp.mail.yahoo.com", 25)

# Set debuglevel to True to show the communication with the server
mail_server.set_debuglevel(True)
try:
    # NOTE: The `sendmail()` method takes the recipient addresses
    # as a list, since a mail can be send to multiple addresses
    # in a single go.
    mail_server.sendmail("arvimal@yahoo.in", ["arvimal@yahoo.in"], message.as_string())
finally:
    mail_server.quit()

# This code printed the logs due to `mail_server.set_debuglevel(True)`
# Since this mail is not authenticated, it failed, obviously.
# To get auth done properly, we'll probably need to use the `authentication`
# mechanisms mentioned in `smtplib.SMTP`
"""
send: 'ehlo [192.168.2.8]\r\n'
reply: b'250-smtp.mail.yahoo.com\r\n'
reply: b'250-PIPELINING\r\n'
reply: b'250-SIZE 41697280\r\n'
reply: b'250-8 BITMIME\r\n'
reply: b'250 STARTTLS\r\n'
reply: retcode (250); Msg: b'smtp.mail.yahoo.com\nPIPELINING\nSIZE 41697280\n8 BITMIME\nSTARTTLS'
send: 'mail FROM:<arvimal@yahoo.in> size=231\r\n'
reply: b'530 5.7.1 Authentication required\r\n'
reply: retcode (530); Msg: b'5.7.1 Authentication required'
send: 'rset\r\n'
reply: b'250 2.0.0 OK\r\n'
reply: retcode (250); Msg: b'2.0.0 OK'
send: 'quit\r\n'
reply: b'221 2.0.0 Bye\r\n'
reply: retcode (221); Msg: b'2.0.0 Bye'
Traceback (most recent call last):
  File "/home/vimal/CODE/Study/100DaysofCode/Day-28/01-smtplib.py", line 41, in <module>
    message.as_string())
  File "/usr/lib64/python3.6/smtplib.py", line 867, in sendmail
    raise SMTPSenderRefused(code, resp, from_addr)
smtplib.SMTPSenderRefused: (530, b'5.7.1 Authentication required', 'arvimal@yahoo.in')
[Finished in 32.7s with exit code 1]
[cmd: ['/usr/bin/python3.6', '/home/vimal/CODE/Study/100DaysofCode/Day-28/01-smtplib.py']]
[dir: /home/vimal/Dropbox/CODE/Study/100DaysofCode/Day-28]
[path: /usr/lib64/qt-3.3/bin:/usr/local/bin:/usr/bin:/bin:/home/vimal/bin:/usr/local/sbin:/usr/sbin]
"""
