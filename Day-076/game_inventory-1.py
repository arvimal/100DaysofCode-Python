#!/usr/bin/env python3

def displayInventory(gamers_inventory):
    """
    Display the gamer's inventory as:
    ---
    Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger

    Total number of items: 63
    ---
    """

    print("\nInventory of *{}*".format(gamers_inventory['name']))
    count = 0
    for key, value in gamers_inventory.items():
        if key is "name":
            pass
        else:
            print("{:>15}: {}".format(key, value))
            count += value
    print("{:>15}: {}".format("Total items", count))


Gamer_1 = {"name" : "Gamer_1", "Arrow" : 10, "Coins" : 40, "Rope" : 1, "Torch" : 2}
Gamer_2 = {"name" : "Gamer_2", "Arrow": 8, "Coins": 20, "Rope": 1, "Torch": 2, "Armor" : 50}
Gamer_3 = {"name": "Gamer_3", "Arrow": 20, "Coins": 50, "Rope": 2, "Torch": 2, "Armor": 150}
Gamer_4 = {"name": "Gamer_4", "Arrow": 28, "Coins": 20, "Rope": 1, "Torch": 12, "Armor": 250}

for name in [Gamer_1, Gamer_2, Gamer_3, Gamer_4]:
    displayInventory(name)
