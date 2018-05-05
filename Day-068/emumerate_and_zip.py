#!/usr/bin/env python3

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i in enumerate(zip(names, countries)):
        print("{}. {:<10} {}".format(i[0] + 1, i[1][0], i[1][1]))
