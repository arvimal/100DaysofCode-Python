#!/usr/bin/env python3

# Differences between the sort() method and sorted() function


games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)

print(games)
print(games_sorted) # The sorted() function returns a new list
print(games.sort()) # The sort() method changes the existing list.
