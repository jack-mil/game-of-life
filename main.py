import sys
import pygame
from settings import Settings


def runGame():
  RED = (255,0,0)
  BLACK = (0,0,0)
  WHITE = (255, 255, 255)
  
  pygame.init()
  values = Settings()
  screen = pygame.display.set_mode((values.screen_width,values.screen_height))
  screen.fill(WHITE)

  def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(values.screen_width):
          for y in range(values.screen_height):
              rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
              pygame.draw.rect(screen, BLACK, rect, 1)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    drawGrid()
    pygame.display.flip()    

    

if __name__ == "__main__":
  runGame()