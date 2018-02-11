#!/usr/bin/env python3

# As per the previous example, the thread started as `daemon`
# will not block the other threads as well as the main program.

# Hence, the main program and other threads will not wait for the 
# daemon thread to exit, before exiting themselves. This may not
# be always good, depending on the requirements.

# The `threading` module thus provides a feature to make the `daemon`
# thread join the main program, and thus make the main program wait 
# for the `daemon` thread to finish, before exiting themselves.

import threading

