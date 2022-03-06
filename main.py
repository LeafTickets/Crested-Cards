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
button = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\Button.png")
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


def drawCard(amount):
    for nums in range(0, amount):
        if deck == []:
            cardPop = 0
            for cards in range(0, len(discard)):
                poppedCard = discard.pop(cardPop)
                deck.append(poppedCard)
        print(deck)
        chosenCard = deck.pop(randint(0, len(deck) - 1))
        hand.append(chosenCard)
        discard.append(chosenCard)


def cardPlace():
    cardSelection = 0
    cardx = 55
    for cards in range(0, len(hand)):
        DISPLAYSURF.blit(hand[cardSelection].cardImage, (cardx, 700))
        cardSelection = cardSelection + 1
        cardx = cardx + 80


deck = [card2, card3, card4, card5, card6]
discard = []
DISPLAYSURF.blit(background, (0, 0))
pygame.display.update()
while start:
    if turn == 0:
        drawn = False
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_a:
                if not drawn:
                    drawCard(2)
                    cardPlace()
                    drawn = True
                    pygame.display.update()
            elif event.type == KEYUP and event.key == K_e:
                 print("CPU's turn")
                 turn = 1
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    elif turn == 1:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                print("Players turn")
                turn = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    else:
        pygame.display.update()
