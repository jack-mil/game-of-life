import sys
import pygame
import math
import numpy as np
from settings import Settings
from cell_rules import GameOfLife, LIVE, DEAD

# GLOBALS
s = Settings()
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
TEAL = (0, 185, 185)
MAGENTA = (200, 0, 100)

screen = pygame.display.set_mode(s.size, flags=pygame.RESIZABLE)
# screen should be global bc it's easier
# repl.it runs 800x600, set in Settings().size
pygame.display.set_caption("The Game of Life")

habitats = s.population


def runGame():
    pygame.init()

    screen.fill(WHITE)

    # Draw initial board
    for x in range(s.screen_width):
        for y in range(s.screen_height):
            rect = pygame.Rect(x * s.block_size,
                               y * s.block_size, s.block_size,
                               s.block_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

    started = False
    initial = set()
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()  # quit on <ESC>

            if event.type == pygame.KEYDOWN:  # start on <RETURN> press for now
                if event.key == pygame.K_RETURN:
                    gol = GameOfLife(habitats.shape[0], habitats.shape[1], initial)
                    started = True
                    print("the game of life has begun")

                if event.key == pygame.K_RIGHT:     # THIS DOES NOT WORK YET
                    gol.evolve()
                    print("evolving")

        # Allow user to change board state if game hasn't started
        if not started:
            # mouse click event to place a square
            # this method allows for press and hold to paint the screen
            left, middle, right = pygame.mouse.get_pressed()

            # get cell the mouse is over currently
            cp = getClickPos()

            # color cell according to pressed button
            if left:
                initial.add(cp)
                print(f"Selected cell {cp}")
                habitats[cp[0], cp[1]] = 1  # sets drawn cell as live in habitat array

            # if right:
            #     drawCell(cp, MAGENTA)

            if middle:
                initial.remove(cp)
                habitats[cp[0], cp[1]] = 0  # sets drawn cell as dead in habitat array


            # draws cell for every living cell found in habitats array
            for row in range(0, habitats.shape[0]):
                for col in range(0, habitats.shape[1]):
                    if habitats[row, col] == 1:
                        drawCell((row, col), TEAL)
                    else:
                        drawCell((row, col), WHITE)
                        drawCell((row, col), BLACK, 1)
        else:
            for y, row in enumerate(gol.cells):
                for x, cell in enumerate(row):
                    if cell.state == LIVE:
                        drawCell((x,y),TEAL)
                    else:
                        drawCell((x, y), WHITE)
                        drawCell((x, y), BLACK, 1)
        pygame.display.flip()

      


def getClickPos():
    """
    Returns whole cell position tuple for the cell under the mouse
    Uses block_size defined in Settings.py
    """
    x, y = pygame.mouse.get_pos()  # get_pos returns an (x, y) tuple of resolution
    cellX = math.floor(x / s.block_size)  # converts resolution to whole cell number
    cellY = math.floor(y / s.block_size)
    return cellX, cellY


def drawCell(position, color, border=0):
    """
    draws a pygame rectangle at the given (x, y) position tuple
    Uses block_size defined in Settings.py
    """
    X = position[0] * s.block_size  # converts cell to rounded resolution
    Y = position[1] * s.block_size
    cell = pygame.Rect(X, Y, s.block_size, s.block_size)
    pygame.draw.rect(screen, color, cell, border)


if __name__ == "__main__":
    runGame()
