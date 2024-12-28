from Grid import Grid


def start_game(x, y):
    grid = Grid.random_colors(x, y)
    grid.get(0, y-1).team = 1
    grid.team1.append(grid.get(0, y-1))
    grid.get(x-1, 0).team = 2
    grid.team2.append(grid.get(x-1, 0))
    return grid


def game_over(grid):
    size = grid.width * grid.height
    if (len(grid.team1) + len(grid.team2)) == size:
        return True
    return False


def choice(grid, col):
    grid.turn_count =+ 1
    grid.num_changed = 0
    if grid.cur_player == 1:
        if col != grid.team1_color and col != grid.team2_color:
            before = len(grid.team1)
            switch_color(grid, col)
            grid.num_changed = len(grid.team1) - before
            return True
        else:
            return False

    elif grid.cur_player == 2:
        if col != grid.team1_color and col != grid.team2_color:
            before = len(grid.team2)
            switch_color(grid, col)
            grid.num_changed = len(grid.team2) - before
            return True
        else:
            return False


def switch_color(grid, col):
    if grid.cur_player == 1:
        for square in grid.team1:
            square.color = col
        grid.team1_color = col
        grow_team(grid, col)
        grid.cur_player = 2
    elif grid.cur_player == 2:
        for square in grid.team2:
            square.color = col
        grid.team2_color = col
        grow_team(grid, col)
        grid.cur_player = 1


def switch_around(grid, x, y, col, t):
    if grid.cur_player == 1:
        if grid.in_bounds(x, y-1) and grid.get(x, y-1).team is None and grid.get(x, y-1).color == col:
            grid.get(x, y - 1).team = 1
            grid.team1.append(grid.get(x, y - 1))
        if grid.in_bounds(x+1, y) and grid.get(x+1, y).team is None and grid.get(x+1, y).color == col:
            grid.get(x+1, y).team = 1
            grid.team1.append(grid.get(x+1,y))
        if grid.in_bounds(x, y+1) and grid.get(x, y+1).team is None and grid.get(x, y+1).color == col:
            grid.get(x, y + 1).team = 1
            grid.team1.append(grid.get(x, y + 1))
        if grid.in_bounds(x-1, y) and grid.get(x-1, y).team is None and grid.get(x-1, y).color == col:
            grid.get(x-1, y).team = 1
            grid.team1.append(grid.get(x-1,y))
    if t == 2:
        if grid.in_bounds(x, y-1) and grid.get(x, y-1).team is None and grid.get(x, y-1).color == col:
            grid.get(x, y - 1).team = 2
            grid.team2.append(grid.get(x, y - 1))
        if grid.in_bounds(x+1, y) and grid.get(x+1, y).team is None and grid.get(x+1, y).color == col:
            grid.get(x+1, y).team = 2
            grid.team2.append(grid.get(x+1,y))
        if grid.in_bounds(x, y+1) and grid.get(x, y+1).team is None and grid.get(x, y+1).color == col:
            grid.get(x, y + 1).team = 2
            grid.team2.append(grid.get(x, y + 1))
        if grid.in_bounds(x-1, y) and grid.get(x-1, y).team is None and grid.get(x-1, y).color == col:
            grid.get(x-1, y).team = 2
            grid.team2.append(grid.get(x-1,y))


def grow_team(grid, col):
    t = grid.cur_player
    if t == 1:
        for square in grid.team1:
            switch_around(grid, square.x, square.y, square.color, t)
    elif t == 2:
        for square in grid.team2:
            switch_around(grid, square.x, square.y, square.color, t)
