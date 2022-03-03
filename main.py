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
placeholder = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\card.png")
background = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\pythonGameBackground.png")
start = True
moved = False
turn = 0
hand = []
hand2 = []


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
    name.cardImage = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images/" + name.name + ".png")
    if type.lower() == "gear":
        name.gearCost = gearCost
        return name
    return name


card3 = cardGenerator("card", 6, "Attack", 8)
card4 = cardGenerator("card", 3, "Attack", 8)
card5 = cardGenerator("card", 3, "Attack", 8)
card6 = cardGenerator("card", 0, "Gear", 4)
deck = [card2, card3, card4, card5, card6]
discard = []



def drawCard(amount):
    for nums in range(0, amount):
        chosenCard = deck.pop(randint(0, len(deck) - 1))
        hand.append(chosenCard)
        discard.append(chosenCard)

DISPLAYSURF.blit(background, (0, 0))
while start:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
    if turn == 0:
        drawCard(2)
        cardSelection = 0
        cardx = 55
        for cards in range(0, len(hand)):
            DISPLAYSURF.blit(hand[cardSelection].cardImage, (cardx, 700))
            cardSelection = cardSelection + 1
            cardx = cardx + 80
        turn = 1
    pygame.display.update()
