#!/usr/bin/env python3

# Regular Expressions, the hard way

def isPhoneNumber(text):
    """
    Identify if the text is a phone number
    """
    if len(text) != 12:
    	return False
    for i in range(0, 3):
    	