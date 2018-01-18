#!/usr/bin/env python3

# Code credit to PyMoTW3
# This is not an exact copy, and was only used as a
# study aid in the process of understanding `smtplib`
# and its use.
import sys
import smtplib
import email.utils
import getpass

from email.mime.text import MIMEText

recipient = input("Recipient address: ")
server_name = input("Mail Server Name: ")
try:
    server_port = int(input("Mail Server Port: "))
except ValueError:
    sys.exit("Expecting an integer as Port number!")


use_tls = input("Use TLS? [Y/N]").lower()
username = input("Username: ")
# Get the password without echoing
password = getpass.getpass("Password for {}: ".format(username))

message = MIMEText("Hello, how are you?")
message.set_unixfrom("Author")
message["To"] = email.utils.format(("Recipient", "recipient"))
message["From"] = email.utils.format(("Author", "arvimal@yahoo.in"))
message["Subject"] = "Test mail"

if use_tls == "y":
    print("Setting up a secure connection.")
    mail_server = smtplib.SMTP(server_name, server_port)
else:
    print("TLS not activated, connection insecure!")
    mail_server = smtplib.SMTP(server_name, server_port)

# Activate the debuglevel
mail_server.set_debuglevel(True)

# The EHLO flag send from the client, will prompt the
# server to send back the features it support, to the
# client.
mail_server.ehlo()

# The `has_extn()` method can be used to list the features
# the server supports. Here, if the server supports TLS, we
# try to use it.

if mail_server.has_extn("STARTTLS"):
    print("Connecting using TLS.")
    mail_server.starttls()
    # We need to use the `EHLO` method once again,
    # to identify ourself for the TLS session
    mail_server.ehlo()
else:
    print("{} does not support TLS".format(server_name))

if mail_server.has_extn('AUTH'):
    print("Trying to authenticate using username/password")
    mail_server.login(username, password)
else:
    print("{} does not support authentication".format(server_name))

mail_server.sendmail("arvimal@yahoo.in",
                     [recipient],
                     message.as_string())

# Quit once the message has been send
mail_server.quit()
