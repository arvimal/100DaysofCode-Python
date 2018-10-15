#!/usr/bin/env python3

def username_generator(first_name, last_name):
  if len(first_name) < 3 and len(last_name) < 4:
    return first_name + last_name
  else:
    return first_name[0:3]  + last_name[0:4]

def password_generator(username):
  return username[-1] + username[0:-1]


user_name = username_generator("Test", "user")
password = password_generator(user_name)

print("{} : {}".format(user_name, password))