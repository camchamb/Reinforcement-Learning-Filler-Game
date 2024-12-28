import copy
from copy import deepcopy
from Particle import *
import random
import numpy as np



class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        self.array = [[None for i in range(width)] for j in range(height)]
        self.team1 = []
        self.team1_color = None
        self.team2 = []
        self.team2_color = None
        self.cur_player = 1
        self.turn_count = 0
        self.num_changed = 0

    def __str__(self):
        return f'Grid({self.width}, {self.height} first = {self.array[0][0]})'

    def __repr__(self):
        return f'Grid.build({self.array})'

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        if type(lst) is not list:
            raise ValueError("Not a list")
        if len(lst) == 0:
            raise ValueError("No elements")
        if lst[0] is None:
            raise ValueError("Empty list")
        for element in lst:
            if type(element) != list:
                raise ValueError("Not a list in the list")
        for i in range(len(lst)-1):
            if len(lst[i]) != len(lst[i+1]):
                raise ValueError("Top level list not equal lengths")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        grid = Grid(width, height)
        grid.array = copy.deepcopy(lst)
        return grid

    def game_over(self):
        size = self.width * self.height
        if self.turn_count > 300:
            print("Game over because of turn count")
            return True
        if (len(self.team1) + len(self.team2)) == size:
            return True
        return False


    def winner(self):
        if len(self.team1) >= len(self.team2):
            return 1
        else:
            return 2

    def copy(self):
        return self.build(self.array)

    def in_bounds(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    def get(self, x, y):
        if not self.in_bounds(x, y):
            raise IndexError
        return self.array[y][x]


    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if not self.in_bounds(x, y):
            raise IndexError
        self.array[y][x] = val


    def get_grid(self):
        total = []
        for lst in self.array:
            colors = []
            for element in lst:
                if element is not None:
                    colors.append(int(element.color))
            total.append(colors)
        return np.array(total).astype(int)


    def get_observation(self):
        total = []
        for lst in self.array:
            colors = []
            for element in lst:
                if element is not None:
                    colors.append(int(element.color))
            total += colors

        return np.array(total).astype(int)


    def get_around(self, x, y, col):
        if self.in_bounds(x - 1, y) and self.get(x - 1, y) is not None and self.get(x - 1, y).color == col:
            return False
        if self.in_bounds(x + 1, y) and self.get(x + 1, y) is not None and self.get(x + 1, y).color == col:
            return False
        if self.in_bounds(x, y-1) and self.get(x , y-1) is not None and self.get(x, y-1).color == col:
            return False
        if self.in_bounds(x, y+1) and self.get(x, y+1) is not None and self.get(x, y+1).color == col:
            return False
        return True


    @staticmethod
    def random_colors(x, y):
        grid = Grid(x, y)
        for i in range(y):
            for j in range(x):
                while True:
                    col = random.randint(0, 5)
                    if grid.get_around(j, i, col):
                        particle = Color(grid, color = col, x= j, y= i)
                        grid.set(j, i, particle)
                        break

        while grid.get(x-1, 0).color == grid.get(0,y-1).color and not grid.get_around(x-1, 0, col):
            col = random.randint(0, 5)
            particle = Color(grid, color=col, x=0, y=y)
            grid.set(0, y-1, particle)

        grid.team1_color = grid.get(0, y-1).color
        grid.team2_color = grid.get(x - 1, 0).color

        return grid


        pass
