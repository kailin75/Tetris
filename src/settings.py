import pygame

# game size
columns = 10
rows = 20
cell_size = 40
game_width, game_height = columns * cell_size, rows *cell_size

# side bar
sidebar_width = 200
preview_height_fraction = 0.7
score_height_fraction = 1 - preview_height_fraction

# entire game field
padding = 20
window_width = game_width + sidebar_width + padding * 3
window_height = game_height + padding * 2

# colors
background = (213, 227, 240)