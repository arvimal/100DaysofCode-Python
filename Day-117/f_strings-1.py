#!/usr/bin/env python3

# F-­strings were first introduced in Python 3.6. 
# If you’re using Python 3.5 or earlier, 
# you’ll need to use the format() method rather than this `f""` syntax.
f_name = "ada"
l_name = "lovelace"

print("F-String string formatting prior python v3.5:- ")
print("\tHello, {} {}".format(f_name.title(), l_name.title()))

print("F-String string formatting from python v3.5:- ")
print(f"\tHello, {f_name.title()} {l_name.title()}")