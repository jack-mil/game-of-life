import sys
import pygame
import math
from settings import Settings

# GLOBALS
settings = Settings()
BLACK = (32,32,32)
WHITE = (255, 255, 255)
TEAL = (0, 185, 185)
MAGENTA = (200, 0, 100)

def runGame():
 
  pygame.init()
  screen = pygame.display.set_mode((settings.screen_width,settings.screen_height)) # rel.it runs 800x600
  pygame.display.set_caption("The Game of Life")
  screen.fill(WHITE)

  for x in range(settings.screen_width):
    for y in range(settings.screen_height):
      rect = pygame.Rect(x*settings.block_size, y*settings.block_size, settings.block_size, settings.block_size)
      pygame.draw.rect(screen, BLACK, rect, 1)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          sys.exit()  # quit on <ESC>
    
    # mouse click event to place a square
    if event.type == pygame.MOUSEBUTTONDOWN:
      cell = getRectFromMouse()

      if event.button == pygame.BUTTON_LEFT:
        pygame.draw.rect(screen, TEAL, cell)

      if event.button == pygame.BUTTON_RIGHT:
        pygame.draw.rect(screen, MAGENTA, cell)
        
      if event.button == pygame.BUTTON_MIDDLE:
        pygame.draw.rect(screen, WHITE, cell)
        pygame.draw.rect(screen, BLACK, cell, 1)
    
    pygame.display.flip()

def getRectFromMouse():
  """ 
  Returns a pygame rectangle object located under the mouse 
  Uses block_size defined in Settings.py
  """

  pos = pygame.mouse.get_pos() # pos is an (x, y) coordinate array
  posX = math.floor(pos[0]/settings.block_size)*settings.block_size # rounds to nearest block corner
  posY = math.floor(pos[1]/settings.block_size)*settings.block_size
  rect = pygame.Rect(posX, posY, settings.block_size, settings.block_size)
  return rect

if __name__ == "__main__":
  runGame()
