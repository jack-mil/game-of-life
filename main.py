import sys
import pygame
import math
import time
from Settings import Settings
from Rules import GameOfLife, LIVE

#     Standard python style guide suggestions:
#     classes use CapitalCase
#     methods/functions use lowerCase
#     variables use lower_case
#     "Constants" use CAPS

# GLOBALS #
s = Settings()
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
TEAL = (0, 185, 185)
MAGENTA = (200, 0, 100)

screen = pygame.display.set_mode(s.size, flags=pygame.RESIZABLE)
pygame.display.set_caption("The Game of Life")

habitats = s.population

pygame.init()


def runGame():
    '''The main pygame runner code'''

    screen.fill(WHITE)
    generation_counter = 0
    started = False
    paused = False
    gen_speed = 0.5

    # Draw initial grid
    for x in range(s.screen_width):
        for y in range(s.screen_height):
            rect = pygame.Rect(x * s.block_size, y * s.block_size,
                               s.block_size, s.block_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Game loop #
    while True:
        for event in pygame.event.get():
            # Quit on SIGterm or <ESC>
            if event.type == pygame.QUIT:
                print("exiting")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("exiting")
                    sys.exit()

            if event.type == pygame.KEYDOWN:

                # Start by pressing <RETURN>
                if event.key == pygame.K_RETURN:
                    gol = GameOfLife(habitats)
                    started = True
                    print("The game of life has begun...")

                # Pause/Un-pause by pressing <SPACE>
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    if paused:
                        print("paused")
                    else:
                        print("resuming")

                # Manually evolve when game is paused
                if started and paused:
                    if event.key == pygame.K_RIGHT:
                        gol.evolve()
                        generation_counter += 1
                        print(f"evolving to generation {generation_counter}")
                        drawGeneration(gol.cells)

            # if event.type == pygame.MOUSEWHEEL:       # Speed change not working yet

        # Edit initial board state #
        if not started:
            # Click/Press and hold mouse to edit
            left, middle, right = pygame.mouse.get_pressed()

            # Get cell that mouse is currently above
            cell_pos = getClickPos()

            if left:
                # Add LIVE cell to initial array
                habitats[cell_pos[0], cell_pos[1]] = 1
                print(f"Selected cell {cell_pos}")

            if middle:
                # Remove DEAD cell from initial array
                habitats[cell_pos[0], cell_pos[1]] = 0
                print(f"Removed cell {cell_pos}")

            # if right:  # maybe have three states in the future ?
            #     habitats[cell_pos[0], cell_pos[1]] = 2

            # Draw LIVE cells found in habitats
            drawGeneration(habitats)

        # Evolve in timed intervals #
        elif not paused:
            time.sleep(gen_speed)
            gol.evolve()
            generation_counter += 1
            print(f"evolving to generation {generation_counter}")

            # Draws LIVE cells found in gol.cells
            drawGeneration(gol.cells)

        # Update the pygame display
        pygame.display.flip()


def getClickPos():
    '''
    Returns whole cell position tuple for the cell under the mouse.
    Uses block_size defined in Settings.py 
    '''
    x, y = pygame.mouse.get_pos()  # get_pos returns an (x, y) tuple of resolution
    pos_x = math.floor(x / s.block_size)  # converts resolution to whole cell number
    pos_y = math.floor(y / s.block_size)
    return pos_x, pos_y


def drawCell(position, color, border=0):
    '''
    Draws a pygame rectangle at the given (x, y) position tuple.
    Uses block_size defined in Settings.py 
    '''
    x = position[0] * s.block_size  # converts cell to rounded resolution
    y = position[1] * s.block_size
    cell = pygame.Rect(x, y, s.block_size, s.block_size)
    pygame.draw.rect(screen, color, cell, border)


def drawGeneration(gen):
    ''' Given a 2d array of cells, draw the cells to the screen. '''

    for y, row in enumerate(gen):
        for x, col in enumerate(row):
            if col == LIVE:
                drawCell((y, x), TEAL)
            else:
                try:
                    if col.state == LIVE:
                        drawCell((y, x), TEAL)
                    else:
                        drawCell((y, x), WHITE)
                        drawCell((y, x), BLACK, 1)
                except AttributeError:
                    drawCell((y, x), WHITE)
                    drawCell((y, x), BLACK, 1)


if __name__ == "__main__":
    runGame()
