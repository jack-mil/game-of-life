import sys
import pygame
import math
from settings import Settings

# GLOBALS
s = Settings()
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
TEAL = (0, 185, 185)
MAGENTA = (200, 0, 100)


def runGame():

    pygame.init()
    # repl.it runs 800x600, set in Settings().size
    screen = pygame.display.set_mode(s.size, flags=pygame.RESIZABLE)  
    pygame.display.set_caption("The Game of Life")
    screen.fill(WHITE)

    for x in range(s.screen_width):
        for y in range(s.screen_height):
            rect = pygame.Rect(x * s.block_size,
                               y * s.block_size, s.block_size,
                               s.block_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()  # quit on <ESC>

        # mouse click event to place a square
        # this method allows for press and hold to paint the screen
        left, middle, right = pygame.mouse.get_pressed()

        # get cell the mouse is over currently
        cell = getRectFromMouse()

        # color cell according to pressed button
        if left:
            pygame.draw.rect(screen, TEAL, cell)

        if right:
            pygame.draw.rect(screen, MAGENTA, cell)
            
        if middle:
            pygame.draw.rect(screen, WHITE, cell)
            pygame.draw.rect(screen, BLACK, cell, 1)

        pygame.display.flip()


def getRectFromMouse():
    """ 
    Returns a pygame rectangle object located under the mouse 
    Uses block_size defined in Settings.py
    """
    x, y = pygame.mouse.get_pos()  # pos is an (x, y) coordinate
    posX = math.floor(x / s.block_size) * s.block_size  # rounds to nearest block corner
    posY = math.floor(y / s.block_size) * s.block_size
    square = pygame.Rect(posX, posY, s.block_size, s.block_size)
    return square


if __name__ == "__main__":
    runGame()
