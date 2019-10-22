#!/usr/bin/env python3


def grade_converter(gpa):
    if gpa >= 4.0:
        grade = "A"
    elif gpa >= 3.0:
        grade = "B"
    elif gpa >= 2.0:
        grade = "C"
    elif gpa >= 1.0:
        grade = "D"
    elif gpa >= 0.0:
        grade = "F"
    return grade


grade_converter(10)
