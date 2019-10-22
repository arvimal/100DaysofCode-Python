#!/usr/bin/env python3

import subprocess

# Use the `run()` method to execute a command without interaction.
command = subprocess.run(["ls", "-l", ".."])

# The `returncode` attribute contains the return status
# of the command. This can either contain an error or a success state.
print("\nReturn status: {}".format(command.returncode))
