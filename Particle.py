"""
code taken from a project at Stanford CS106A
"""

import datetime
import tkinter

# from Grid import Grid



"""Insert the Sand class here"""
class Color:
    def __init__(self, grid, color=None, x=0, y=0):
        self.grid = grid
        self.x, self.y = x, y
        self.color = color
        self.team = None

    def __str__(self):
        return f"Color:{self.color}:{self.x},{self.y}"

    def is_move_ok(self, x_to, y_to):
        if not self.grid.in_bounds(x_to, y_to):
            return False
        if not (self.grid.get(x_to, y_to) is None):
            return False
        if self.x != x_to:
            if not (self.grid.get(x_to, self.y) is None):
                return False
        return True
        pass