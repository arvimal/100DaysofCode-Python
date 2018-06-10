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
    for key, value in gamers_inventory.items():
        if key is "name":
            pass
        else:
            print("{:>10} {}".format(value, key))


gamer_1 = {"name" : "gamer_1", "Arrow" : 10, "Coins" : 40, "Rope" : 1, "Torch" : 2}
gamer_2 = {"name" : "gamer_2", "Arrow": 8, "Coins": 20, "Rope": 1, "Torch": 2, "Armor" : 50}
gamer_3 = {"name": "gamer_3", "Arrow": 20, "Coins": 50, "Rope": 2, "Torch": 2, "Armor": 150}
gamer_4 = {"name": "gamer_4", "Arrow": 28, "Coins": 20, "Rope": 1, "Torch": 12, "Armor": 250}

for name in [gamer_1, gamer_2, gamer_3, gamer_4]:
    displayInventory(name)
