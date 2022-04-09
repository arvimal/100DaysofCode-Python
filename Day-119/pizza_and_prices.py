#!/usr/bin/env python3
# Path: Day-119/pizza_and_prices.py

toppings = [
    "pepporoni",
    "pineapple",
    "cheese",
    "sausage",
    "olives",
    "anchovies",
    "mushrooms",
]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = []
for topping in toppings:
    price = prices[toppings.index(topping)]
    pizza_and_prices.append([price, topping])

for i in pizza_and_prices:
    print(i)
