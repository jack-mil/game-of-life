import sys
import pygame
from settings import Settings


WHITE = (200, 200, 200)
RED = (255,0,0)

def runGame():
  pygame.init()
  values = Settings()
  screen = pygame.display.set_mode((values.screen_width,values.screen_height))
  screen.fill(values.bg_color)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    screen.fill(RED)
    # drawGrid()

  pygame.display.flip()    
    
def drawGrid():
  values = Settings()
  blockSize = 20 #Set the size of the grid block
  for x in range(values.screen_width):
        for y in range(values.screen_height):
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

if __name__ == "__main__":
  runGame()