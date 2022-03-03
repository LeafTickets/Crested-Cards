import pygame, sys
from pygame.locals import *
import os

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 900))
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
    damage = 0
    gearCost = 0
    cardType = "Placeholder"


card2 = card("Basic Attack")
card2.damage = 5
card2.cardImage = placeholder
def cardGenerator(name, damage, type, gearCost):
  name = card(name)
  name.damage = damage
  name.cardType = type
  name.cardImage = pygame.image.load("/home/runner/pythonGame-1/Images/"+name.name+".jpg")
  if type.lower() == "gear":
    name.gearCost = gearCost
    return name
  return name
card3 = cardGenerator("Stab_Attack", 6, "Attack", 8)
DISPLAYSURF.blit(background, (0, 0))
DISPLAYSURF.blit(card3.cardImage, (50, 50))
while True:
  for event in pygame.event.get():
    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
      pygame.quit()
      sys.exit()
  pygame.display.update()
