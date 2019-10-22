#!/usr/bin/env python3

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)


def graduation_reqs(gpa, credits):
    if credits >= 120 and gpa >= 2.0:
        return "You meet the requirements to graduate!"


print(graduation_reqs(1.0, 125))
print(graduation_reqs(1.4, 15))
print(graduation_reqs(5.0, 155))
