import pygame, sys
from pygame.locals import *
import os

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption('Game Window')
purple = pygame.Color(128, 0, 128)
black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 0)
mousex = 0
mousey = 0
moving = False
placeholder = pygame.image.load("/home/runner/pythonGame-1/Images/Square.png")
background = pygame.image.load("/home/runner/pythonGame-1/Images/pythonGameBackground.png")


class card:
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    cardImage = placeholder
    damage = 1
    gearCost = 0


card2 = card("Basic Attack")
card2.damage = 5
card2.cardImage = placeholder
def main():
  DISPLAYSURF.blit(background, (0, 0))
  while True:
      for event in pygame.event.get():
          if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
  pygame.display.update()

main()