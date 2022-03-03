import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Game Window')
purple = pygame.Color(128, 0, 128)
black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 0)
mousex = 0
mousey = 0
placeholder = pygame.image.load(r"C:\Users\jair1966\PycharmProjects\pythonGame\Images\Square.png")
background = pygame.image.load(r"C:\Users\jair1966\PycharmProjects\pythonGame\Images\pythonGameBackground.png")
start = True
moved = False
turn = 0
hand = []


class card:
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    cardImage = placeholder
    damage = 0
    gearCost = 0
    cardType = "Placeholder"
    moving = False


card2 = card("Basic Attack")
card2.damage = 5
card2.cardImage = placeholder


def cardGenerator(name, damage, type, gearCost):
    name = card(name)
    name.damage = damage
    name.cardType = type
    name.cardImage = pygame.image.load(r"C:\Users\jair1966\PycharmProjects\pythonGame\Images/" + name.name + ".png")
    if type.lower() == "gear":
        name.gearCost = gearCost
        return name
    return name


card3 = cardGenerator("Stab_Attack", 6, "Attack", 8)
card4 = cardGenerator("Basic_Attack", 3, "Attack", 8)
card5 = cardGenerator("Basic_Attack", 3, "Attack", 8)
card6 = cardGenerator("Basic_Attack", 0, "Gear", 4)
deck = [card2, card3, card4, card5, card6]
discard = []

def drawCard(amount):
    for nums in range(0, amount):
        chosenCard = deck.pop(randint(0, len(deck)))
        hand.append(chosenCard)
        discard.append(chosenCard)

DISPLAYSURF.blit(background, (0, 0))
DISPLAYSURF.blit(card3.cardImage, (50, 50))
while start:
    DISPLAYSURF.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
    if turn == 0:
        turn = 1
        drawCard(2)
        print(hand)
    pygame.display.update()
