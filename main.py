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
drawn = False


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


card3 = cardGenerator("card", 6, "Attack", -8)
card4 = cardGenerator("card", 3, "Attack", -8)
card5 = cardGenerator("card", 3, "Attack", -8)
card6 = cardGenerator("card1", 0, "Gear", 4)
card7 = cardGenerator("card1", 50, "Gear", -5)
card8 = cardGenerator("card", 3, "Attack", -8)
card9 = cardGenerator("card", 3, "Attack", -8)
card10 = cardGenerator("card", 3, "Attack", -8)


def drawCard(amount):
    for nums in range(0, amount):
        if len(hand) == 9:
            return
        if deck == []:
            if discard == []:
                return
            cardPop = 0
            for cards in range(0, len(discard)):
                poppedCard = discard.pop(cardPop)
                deck.append(poppedCard)
        print(deck)
        chosenCard = deck.pop(randint(0, len(deck) - 1))
        hand.append(chosenCard)


def cardPlace():
    cardSelection = 0
    cardx = 55
    for cards in range(0, len(hand)):
        DISPLAYSURF.blit(hand[cardSelection].cardImage, (cardx, 700))
        cardSelection = cardSelection + 1
        cardx = cardx + 80


def playCard(chosenCard, gears, health):  # for target, the player is 1 while the enemy is 0
    discardedCard = hand.pop(hand.index(chosenCard))
    discard.append(discardedCard)
    print(discard)
    value1 = health
    value2 = gears
    if chosenCard.damage > 0:
        value1 = health - chosenCard.damage
    if chosenCard.gearCost > 0:
        value2 = gears + chosenCard.gearCost
    if chosenCard.gearCost < 0:
        if abs(chosenCard.gearCost) > gears:
            return health, gears
        elif abs(chosenCard.gearCost) <= gears:
            value2 = gears + chosenCard.gearCost
    return value1, value2

def displayUpdate():
    if hand == []:
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(discard[-1].cardImage, (1100, 500))
    else:
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(hand[0].cardImage, (1100, 500))

def getCard():
  cardChecked = 0
  for cards in range(0, len(hand)):
    rect = hand[cardChecked].cardImage.get_rect(x=300, y=100)
    if rect.collidepoint(pygame.mouse.get_pos()):
      return hand[cardChecked]
    cardChecked = cardChecked + 1

enemyHealth = 100
enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
playerHealth = 100
currentGears = 0
deck = [card2, card3, card4, card5, card6, card7, card8, card9, card10]
discard = []
DISPLAYSURF.blit(background, (0, 0))
pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
pygame.display.update()
while start:
    if turn == 0:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_a:
                if not drawn:
                    drawCard(3)
                    cardPlace()
                    drawn = True
                    pygame.display.update()
            elif event.key == K_e:
                print("CPU's turn")
                turn = 1
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_1:
                enemyHealth, currentGears = playCard(hand[0], currentGears, enemyHealth)
            elif event.key == K_2:
                enemyHealth, currentGears = playCard(hand[1], currentGears, enemyHealth)
            elif event.key == K_3:
                enemyHealth, currentGears = playCard(hand[2], currentGears, enemyHealth)
            elif event.key == K_4:
                enemyHealth, currentGears = playCard(hand[3], currentGears, enemyHealth)
            elif event.key == K_5:
                enemyHealth, currentGears = playCard(hand[4], currentGears, enemyHealth)
            elif event.key == K_6:
                enemyHealth, currentGears = playCard(hand[5], currentGears, enemyHealth)
            elif event.key == K_7:
                enemyHealth, currentGears = playCard(hand[6], currentGears, enemyHealth)
            elif event.key == K_8:
                enemyHealth, currentGears = playCard(hand[7], currentGears, enemyHealth)
            elif event.key == K_9:
                enemyHealth, currentGears = playCard(hand[8], currentGears, enemyHealth)
            displayUpdate()
            enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
            cardPlace()
            pygame.display.update()
            print(enemyHealth, currentGears)
        elif event.type == MOUSEBUTTONUP:
            print(getCard())
            enemyHealth, currentGears = playCard(hand[getCard()], currentGears, enemyHealth)
            displayUpdate()
            enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
            cardPlace()
            pygame.display.update()
            print(enemyHealth, currentGears)
    elif turn == 1:
        drawn = False
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_a:
                print("Players turn")
                turn = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if enemyHealth <= 0:
        pygame.quit()
        sys.exit()
    else:
        pygame.display.update()
