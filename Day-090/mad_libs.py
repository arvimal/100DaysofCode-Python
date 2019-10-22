#!/usr/bin/env python3

"""
Mad Libs program in Python

The gist is to probe the user for several inputs, and add them in
the STORY template.

The output turn outs to be usually funny.
"""

# The Story template

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."


print("Starting Mad Libs")
name = input("Enter a name: ")

adj1 = input("Enter the first adjective: ")
adj2 = input("Enter the second adjective: ")
adj3 = input("Enter the third adjective: ")

verb1 = input("Enter a verb: ")

noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")

animal = input("Enter an Animal name: ")
food = input("Enter a food name: ")
fruit = input("Enter a fruit name: ")
superhero = input("Enter a superhero name: ")
country = input("Enter a country name: ")
dessert = input("Enter a dessert name: ")
year = input("Enter a year: ")


print(
    STORY
    % (
        name,
        adj1,
        adj2,
        animal,
        food,
        verb1,
        noun1,
        fruit,
        adj3,
        name,
        superhero,
        name,
        country,
        name,
        dessert,
        name,
        year,
        noun2,
    )
)
