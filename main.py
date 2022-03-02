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
    cardImage = image
    damage = 1
    gearCost = 0


card.cardImage = image2

while True:
    mouseClicked = False
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
    while mouseClicked:
        mousex, mousey = event.pos
        DISPLAYSURF.fill(black)
        DISPLAYSURF.blit(card.cardImage, (mousex - 200, mousey - 200))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = False
        pygame.display.update()
    pygame.display.update()
