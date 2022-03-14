import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()  # Starts pygame
DISPLAYSURF = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('pythonGame')
purple = pygame.Color(128, 0, 128)
black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 0)
mousex = 0
mousey = 0
placeholder = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\card.png")
ambientBackground = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\placeholder.png")
background = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\gui.png")
button = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images\Button.png")
playerHealth = 100
start = True
moved = False
turn = 0
hand2 = []
drawn = False
inCombat = False


class card:  # All the cards info is stored here
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    cardImage = placeholder
    damage = 0
    gearCost = 0
    cardType = "Placeholder"
    weight = 0


hand = []
discard = []
currentGears = 0
health = 100
copper = 0
iron = 0
silver = 0


class encounter:
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    health = 50
    currentGears = 3
    deck = []
    discard = []
    hand = []
    encounterImage = placeholder


def cardGenerator(name, damage, type, gearCost):  # makes a new card
    name = card(name)
    name.damage = damage
    name.cardType = type
    name.cardImage = pygame.image.load(r"C:\Users\streambox-31\PycharmProjects\pythonGame\Images/" + name.name + ".png")
    if type.lower() == "gear":
        name.gearCost = gearCost
        return name
    return name


def encounterGenerator(name, health, startingGears):
    name = encounter(name)
    name.health = health
    name.encounterImage = pygame.image.load(
        r"C:\Users\streambox-31\PycharmProjects\pythonGame\encounterImages/" + name.name + ".png")
    name.currentGears = startingGears
    return name


card3 = cardGenerator("card", 6, "Attack", -8)
card4 = cardGenerator("card", 3, "Attack", -8)
card5 = cardGenerator("card", 3, "Attack", -8)
card6 = cardGenerator("card2", 0, "Gear", 4)
card7 = cardGenerator("card1", 50, "Gear", -5)
card8 = cardGenerator("card", 3, "Attack", -8)
card9 = cardGenerator("card", 3, "Attack", -8)
card10 = cardGenerator("card", 3, "Attack", -8)

encounter2 = encounterGenerator("Mimic", 50, 3)


def drawCard(amount, target):  # draws a certain amount of cards
    if target == 0:
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
            chosenCard = deck.pop(randint(0, len(deck) - 1))
            hand.append(chosenCard)
    if target == 1:
        for nums in range(0, amount):
            if len(hand2) == 9:
                return
            if edeck == []:
                if ediscard == []:
                    return
                cardPop = 0
                for cards in range(0, len(discard)):
                    poppedCard = ediscard.pop(cardPop)
                    edeck.append(poppedCard)
            chosenCard = edeck.pop(randint(0, len(edeck) - 1))
            hand2.append(chosenCard)


def cardPlace():  # Places the cards in the hand on the screen
    cardSelection = 0
    cardx = 55
    for cards in range(0, len(hand)):
        DISPLAYSURF.blit(hand[cardSelection].cardImage, (cardx, 700))
        cardSelection = cardSelection + 1
        cardx = cardx + 80


def playCard(chosenCard, gears, health, target):  # for target, the player is 0 while the enemy is 1
    if target == 1:
        discardedCard = hand.pop(hand.index(chosenCard))
        discard.append(discardedCard)
    if target == 0:
        discardedCard = hand2.pop(0)
        ediscard.append(discardedCard)
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


def getWeight(card):
    return card.weight


def autoPlayCard(hand, health, gears):
    cardNum = 0
    for cards in range(0, len(hand)):
        cardChosen = hand[cardNum]
        cardChosen.weight = 0
        if cardChosen.cardType == "Gear":
            if cardChosen.gearCost > 0:
                cardChosen.weight = cardChosen.weight + 5
            if cardChosen.gearCost < 0:
                cardChosen.weight = cardChosen.weight + 3
        if cardChosen.cardType == "Attack":
            if cardChosen.damage > 5:
                cardChosen.weight = cardChosen.weight + 2
            else:
                cardChosen.weight = cardChosen.weight + 1
        cardNum = cardNum + 1
    hand.sort(key=getWeight, reverse=True)
    value1 = health
    value2 = gears
    for cards in range(0, len(hand)):
        displayUpdate()
        pygame.display.update()
        pygame.time.delay(100)
        DISPLAYSURF.blit(hand[0].cardImage, (500, 500))
        pygame.display.update()
        pygame.time.delay(500)
        value1, value2 = playCard(hand[0], value2, value1, 0)
    return value1, value2


def displayUpdate():  # updates the display for all the cards and background
    if hand == []:
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(discard[-1].cardImage, (1100, 500))
        DISPLAYSURF.blit(encounter2.encounterImage, (300, 150))
        enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
        playerHeathBar = pygame.Rect((20, 629), (playerHealth, 20))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), playerHeathBar)
    else:
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(hand[0].cardImage, (1100, 500))
        DISPLAYSURF.blit(encounter2.encounterImage, (300, 150))
        enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
        playerHeathBar = pygame.Rect((20, 629), (playerHealth, 20))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), playerHeathBar)


def getCard():  # gets the card under the mouse
    cardChecked = 0
    x = 55
    y = 700
    for cards in range(0, len(hand)):
        rect = hand[cardChecked].cardImage.get_rect(x=x, y=y)
        if rect.collidepoint(pygame.mouse.get_pos()):
            return cardChecked
        cardChecked = cardChecked + 1
        x = x + 80


def encounterLoad():
    health = encounter2.health
    pygame.display.update()
    return health


enemyHealth = 100
enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
playerHeathBar = pygame.Rect((100, 100), (playerHealth, 20))
deck = [card3, card4, card5, card6, card7, card8, card9, card10]
edeck = [card3, card4, card5, card6, card7, card8, card9, card10]
ediscard = []
DISPLAYSURF.blit(background, (0, 0))
pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
pygame.display.update()
while start:  # Main loop for the game
    if inCombat:
        pygame.display.update()
        if turn == 0:  # Players turn
            if not drawn:
                drawCard(3, 0)
                cardPlace()
                drawn = True
                pygame.display.update()
            pygame.event.clear()
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_e:
                    print("CPU's turn")
                    turn = 1
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = pygame.mouse.get_pos()
                if mousey > 800 or mousey < 700:
                    enemyHealth, currentGears = enemyHealth, currentGears
                elif mousex > (len(hand) * 80) + 55 or mousex < 55:
                    enemyHealth, currentGears = enemyHealth, currentGears
                else:
                    enemyHealth, currentGears = playCard(hand[getCard()], currentGears, enemyHealth, 1)
                displayUpdate()
                cardPlace()
                pygame.display.update()
                print(enemyHealth, currentGears)
        elif turn == 1:  # CPU's turn
            drawn = False
            drawCard(3, 1)
            playerHealth, encounter2.currentGears = autoPlayCard(hand2, playerHealth, encounter2.currentGears)
            displayUpdate()
            pygame.display.update()
            print(playerHealth)
            pygame.event.clear()
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            turn = 0
        if enemyHealth <= 0:
            inCombat = False
        if playerHealth <= 0:
            pygame.quit()
            sys.exit()
        else:
            pygame.display.update()
    elif not inCombat:
        DISPLAYSURF.blit(ambientBackground, (0, 0))
        pygame.display.update()
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == MOUSEBUTTONUP:
            enemyHealth = encounterLoad()
            deck = [card3, card4, card5, card6, card7, card8, card9, card10]
            hand = []
            discard = []
            drawn = False
            currentGears = 0
            DISPLAYSURF.blit(background, (0, 0))
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
            pygame.display.update()
            inCombat = True
