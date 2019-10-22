#!/usr/bin/env python3


def graduation_reqs(gpa, credits):
    if (gpa >= 2.0) and (credits >= 120):
        return "You meet the requirements to graduate!"
    elif (gpa >= 2.0) and not (credits >= 120):
        return "You do not have enough credits to graduate."
    elif not (gpa >= 2.0) and (credits >= 120):
        return "Your GPA is not high enough to graduate."
    else:
        return "You do not meet the GPA or the credit requirement for graduation."
