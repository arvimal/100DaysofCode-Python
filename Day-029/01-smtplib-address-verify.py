#!/usr/bin/env python3

# Verify a mail address with a mail server.

# Mail servers can be probed to understand if a
# mail address exist or not. By default, it's disabled.

# The `verify()` method from `smtplib.SMTP()` sends the
# `VRFY` flag to the server.

# Since this feature is disabled on almost all SMTP servers
# by default, the server may reply back with either an
# Invalid command or `user` not available.

import smtplib

mail_server = smtplib.SMTP("smtp.mail.yahoo.com", 25)
mail_server.set_debuglevel(True)

try:
    verify_mail = mail_server.verify("arvimal")
    print(verify_mail)
finally:
    mail_server.quit()
