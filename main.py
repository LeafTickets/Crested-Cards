import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1080, 900))
pygame.display.set_caption('Hello World!')
purple = pygame.Color(128, 0, 128)
black = pygame.Color(0, 0, 0)
mousex = 0
mousey = 0
image = pygame.image.load("Square.png")
image2 = pygame.image.load("image2.jpg")
moving = False


class card:
  def __init__(self, nam):
    self.name = nam
    print(self.name,'constructed')
  cardImage = image
  damage = 1
  gearCost = 0


card2 = card("Basic Attack")
card2.damage = 5
card2.cardImage = image2
print(card2.name)

while True:
    mouseClicked = False
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif (event.type == KEYUP and event.key == K_a) or (event.type == KEYUP and event.key == K_s):
            mouseClicked = True
    while mouseClicked:
        for event in pygame.event.get():
              if (event.type == KEYUP and event.key == K_a):
                DISPLAYSURF.fill(black)
                DISPLAYSURF.blit(card2.cardImage, (mousex - 200, mousey - 200))
                mouseClicked = False
              elif (event.type == KEYUP and event.key == K_s):
                DISPLAYSURF.fill(black)
                DISPLAYSURF.blit(card.cardImage, (mousex - 200, mousey - 200))
                mouseClicked = False
              else:  
                pygame.display.update()
        pygame.display.update()
    pygame.display.update()
