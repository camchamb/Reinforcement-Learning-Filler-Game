"""
code based from a project at Stanford CS106A
"""
from Grid import Grid
from Filler_Game import * # imports all Grid objects
from Particle import Color
import random
import pygame

# Set up some constants
HEADER_THICKNESS = 40 # thickness of header menu bar in pixels
WIDTH, HEIGHT = 500, 400 # 500 x 500 for simulation, 100 pixel header for buttons
SCALE = 50 # pixels per particle

BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
LIGHT_GRAY = (240, 240, 240)

FONT = None

def mainloop(grid, window):
    # Game loop
    running = True

    # Button surfaces
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] < HEADER_THICKNESS: # menu button press
                if 0 < event.pos[0] < 83:
                    col =0
                elif 83 < event.pos[0] < 166:
                    col =1
                elif 166 < event.pos[0] < 249:
                    col =2
                elif 249 < event.pos[0] < 332:
                    col = 3
                elif 332 < event.pos[0] < 415:
                    col =4
                elif 415 < event.pos[0] < 500:
                    col = 5

                if grid.cur_player == 1:
                    if col != grid.team1_color and col != grid.team2_color:
                        switch_color(grid, col)

                elif grid.cur_player == 2:
                    if col != grid.team1_color and col != grid.team2_color:
                        switch_color(grid, col)

                update_buttons(grid)

        draw_simulation(window, grid)
        draw_header(window)
        pygame.display.flip()


def draw_simulation(window, grid):
    # Draw everything
    window.fill(LIGHT_GRAY)
    for y in range(grid.height):
        for x in range(grid.width):
            val = grid.get(x, y)
            if val:
                if isinstance(val, Color):
                    col = val.color
                    if col == 0:
                        cell = RED
                    if col == 1:
                        cell = GREEN
                    if col == 2:
                        cell = YELLOW
                    if col == 3:
                        cell = LIGHT_BLUE
                    if col == 4:
                        cell = PURPLE
                    if col == 5:
                        cell = BLACK
                    else:
                        # cell = WHITE
                        pass
                pygame.draw.rect(window, cell, pygame.Rect(x * SCALE, HEADER_THICKNESS + y * SCALE, SCALE, SCALE))
    pygame.draw.rect(window, BLACK, pygame.Rect(0, HEADER_THICKNESS, WIDTH, HEIGHT-HEADER_THICKNESS), 1)


def draw_header(window):
    pygame.draw.rect(window, BLACK, pygame.Rect(0, 0, WIDTH//6, HEADER_THICKNESS+1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(WIDTH // 6, 0, WIDTH // 6, HEADER_THICKNESS + 1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(2*WIDTH // 6, 0, WIDTH // 6, HEADER_THICKNESS + 1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(3 * WIDTH // 6 -1, 0, WIDTH // 6, HEADER_THICKNESS + 1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(4 * WIDTH // 6 - 1, 0, WIDTH // 6, HEADER_THICKNESS + 1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(5 * WIDTH // 6 - 1, 0, WIDTH - 1, HEADER_THICKNESS + 1), 1)
    pygame.draw.rect(window, BLACK, pygame.Rect(5 * WIDTH // 6 - 50, HEADER_THICKNESS, WIDTH - 1, HEADER_THICKNESS + 1), 1)
    window.blit(B_RED, (20, 10))
    window.blit(B_GREEN, (93, 10))
    window.blit(B_YELLOW, (176, 10))
    window.blit(B_BLUE, (269, 10))
    window.blit(B_PURPLE, (342, 10))
    window.blit(B_BLACK, (425, 10))
    window.blit(B_PLAYER, (400, 50))
    window.blit(B_SCORE1, (400, 90))
    window.blit(B_SCORE2, (400, 130))

def update_buttons(grid):
    global B_RED, B_GREEN, B_YELLOW, B_BLUE, B_PURPLE, B_BLACK, B_PLAYER, B_SCORE1, B_SCORE2
    B_RED = FONT.render("RED", True, BLACK, LIGHT_GRAY)
    B_BLUE = FONT.render("BLUE", True, BLACK, LIGHT_GRAY)
    B_GREEN = FONT.render("GREEN", True, BLACK, LIGHT_GRAY)
    B_YELLOW = FONT.render("YELLOW", True, BLACK, LIGHT_GRAY)
    B_PURPLE = FONT.render("PURPLE", True, BLACK, LIGHT_GRAY)
    B_BLACK = FONT.render("BLACK", True, BLACK, LIGHT_GRAY)
    B_SCORE1 = FONT.render(f"1: {len(grid.team1)}", True, BLACK, LIGHT_GRAY)
    B_SCORE2 = FONT.render(f"2: {len(grid.team2)}", True, BLACK, LIGHT_GRAY)
    if game_over(grid):
        if len(grid.team1) > len(grid.team2):
            B_PLAYER = FONT.render("P1 WON", True, BLACK, LIGHT_GRAY)
        else:
            B_PLAYER = FONT.render("P2 WON", True, BLACK, LIGHT_GRAY)
    elif isinstance(grid, int) or grid.cur_player == 1:
        B_PLAYER = FONT.render("PLAYER: 1", True, BLACK, LIGHT_GRAY)
    elif grid.cur_player == 2:
        B_PLAYER = FONT.render("PLAYER: 2", True, BLACK, LIGHT_GRAY)
    else:
        B_PLAYER = FONT.render("PLAYER: ?", True, BLACK, LIGHT_GRAY)


    if game_over(grid):
        B_SCORE = FONT.render("GAME OVER", True, BLACK, LIGHT_GRAY)
    else:
        B_SCORE = FONT.render(f"{len(grid.team1)}", True, BLACK, LIGHT_GRAY)


def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    global FONT
    FONT = pygame.font.SysFont("Arial", 20)

    # Create game state
    grid = start_game(7, 7)
    update_buttons(grid)

    # Create the window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Simulation")

    mainloop(grid, window)


if __name__ == "__main__":
    main()