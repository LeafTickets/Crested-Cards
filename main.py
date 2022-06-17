import pygame
import sys
from pygame.locals import *
from random import randint
from crestFunctions import crestActivator
import os

pygame.init()  # Starts pygame
DISPLAYSURF = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('pythonGame')
purple = pygame.Color(128, 0, 128)
black = pygame.Color(0, 0, 0)
white = pygame.Color(0, 0, 0)
mousex = 0
mousey = 0
directory = os.getcwd()
placeholder = pygame.image.load(directory + "/Images/card.png")
ambientBackground = pygame.image.load(directory + "/Images/main menu.png")
background = pygame.image.load(directory + "/Images/Untitled drawing.png")
background2 = pygame.image.load(directory + "/Images/bg.png")
button = pygame.image.load(directory + "/Images/Button.png")
playerHealth = 100
start = True
moved = False
turn = 0
hand2 = []
drawn = False
inCombat = False
font = pygame.font.Font('freesansbold.ttf', 16)
crests = ["none", "none", "none", "none"]


class crest:
    def __init__(self, nam, effects, spot):
        self.name = nam
        self.effects = effects  # List order, health, gears, copper, iron, silver
        self.crestSpot = spot
        print(self.name, 'constructed')


class card:  # All the card's info is stored here
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    cardImage = placeholder
    damage = 0
    gearCost = 0
    cardType = "Placeholder"
    weight = 0
    crestEffects = "none"


hand = []
discard = []
crestDiscard = []
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


def cardGenerator(name, damage, type, gearCost, effects=None, spot=0):  # makes a new card
    if effects is None:
        effects = []
    name = card(name)
    name.damage = damage
    name.cardType = type
    name.cardImage = pygame.image.load(directory + "/Images/" + name.name + ".png")
    if type.lower() == "gear":
        name.gearCost = gearCost
        return name
    if type.lower() == "crest":
        name.crestEffects = crest(name, effects, spot)
    return name


def encounterGenerator(name, health, startingGears):
    name = encounter(name)
    name.health = health
    name.encounterImage = pygame.image.load(
        directory + "/encounterImages/" + name.name + ".png")
    name.currentGears = startingGears
    return name


card3 = cardGenerator("Basic_AttackLv3", 6, "Attack", -8)
card4 = cardGenerator("Basic_AttackLv2", 3, "Attack", -8)
card5 = cardGenerator("Basic_AttackLv2", 3, "Attack", -8)
card6 = cardGenerator("Disassemble", 0, "Gear", 4)
card7 = cardGenerator("Gear_Burst", 50, "Gear", -5)
card8 = cardGenerator("Basic_AttackLv2", 3, "Attack", -8)
card9 = cardGenerator("Basic_AttackLv2", 3, "Attack", -8)
card10 = cardGenerator("Basic_AttackLv2", 3, "Attack", -8)
crest1 = cardGenerator("Mechanized_Healing", 0, "Crest", -8, [5, -1, 0, 0, 0], 0)
crest2 = cardGenerator("Copper_Gear_Factory", 0, "Crest", -8, [0, 1, -1, 0, 0], 1)

encounter1 = encounterGenerator("Mimic", 75, 1)
encounter2 = encounterGenerator("eneny", 50, 3)

encounters = [encounter1, encounter2]

deck = [card3, card4, card5, crest1, card6, card7, card8, card9, card10, crest2]
edeck = [card3, card4, card5, card6, card7, card8, card9, card10]
ediscard = []


def drawCard(amount, target):  # draws a certain amount of cards
    if target == 0:
        for nums in range(0, amount):
            if len(hand) == 9:
                return
            if not deck:
                if not discard:
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
            if not edeck:
                cardPop = 0
                if not ediscard:
                    return
                else:
                    for cards in range(0, len(discard)):
                        if not ediscard:
                            return
                        poppedCard = ediscard.pop(cardPop)
                        edeck.append(poppedCard)
            chosenCard = edeck.pop(randint(0, len(edeck) - 1))
            hand2.append(chosenCard)


def cardPlace(cardx=55, cardy=785):  # Places the cards in the hand on the screen
    cardSelection = 0
    for cards in range(0, len(hand)):
        DISPLAYSURF.blit(hand[cardSelection].cardImage, (cardx, cardy))
        cardSelection = cardSelection + 1
        cardx = cardx + 80


def crestChecker(crest):
    if crests[crest.crestEffects.crestSpot] != 'none':
        poppedCrest = crests.pop(crests.index(crest))
        crests.append()
        discard.append(poppedCrest)


def playCard(chosenCard, gears, health, target):  # for target, the player is 0 while the enemy is 1
    if target == 1:
        discardedCard = hand.pop(hand.index(chosenCard))
        if discardedCard.cardType == "Crest":
            crestChecker(chosenCard)
            crestDiscard.append(discardedCard)
        else:
            discard.append(discardedCard)
    if target == 0:
        discardedCard = hand2.pop(0)
        ediscard.append(discardedCard)
    value1 = health
    value2 = gears
    if chosenCard.cardType == "Crest":
        if len(crests) > 4:
            return
        crests[chosenCard.crestEffects.crestSpot] = chosenCard.crestEffects
        print(crests)
        return value1, value2
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
                cardChosen.weight = cardChosen.weight + 7
            if cardChosen.gearCost < 0:
                cardChosen.weight = cardChosen.weight + 4
        if cardChosen.cardType == "Attack":
            if cardChosen.damage > 5:
                cardChosen.weight = cardChosen.weight + 3
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
    if not hand:
        DISPLAYSURF.blit(background2, (0, 0))
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(discard[-1].cardImage, (1030, 600))
        DISPLAYSURF.blit(encounter2.encounterImage, (300, 150))
        enemyHealthBar = pygame.Rect((1000, 100), (enemyHealth, 25))
        playerHeathBar = pygame.Rect((20, 629), (playerHealth, 20))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), playerHeathBar)
    else:
        DISPLAYSURF.blit(background2, (0, 0))
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(hand[0].cardImage, (1030, 600))
        DISPLAYSURF.blit(encounter2.encounterImage, (300, 150))
        enemyHealthBar = pygame.Rect((1000, 100), (enemyHealth, 25))
        playerHeathBar = pygame.Rect((20, 629), (playerHealth, 20))
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), playerHeathBar)


def getCard(x=55, y=785):  # gets the card under the mouse
    cardChecked = 0
    for cards in range(0, len(hand)):
        rect = hand[cardChecked].cardImage.get_rect(x=x, y=y)
        if rect.collidepoint(pygame.mouse.get_pos()):
            return cardChecked
        cardChecked = cardChecked + 1
        x = x + 80


def encounterLoad(encounter):
    health = encounter.health
    startingGears = encounter.currentGears
    pygame.display.update()
    return health, startingGears


def randomLootGenerator(amount):
    x = 520
    y = 450
    drawnCards = []
    cardTypes = ['gear+', 'crest', 'attack', 'gear-']
    for cards in range(amount):
        cardType = cardTypes[randint(0, 2)]
        if cardType == 'attack':
            card1 = cardGenerator("card", randint(0, 6), "Attack", -8)
        elif cardType == 'gear+':
            card1 = cardGenerator("card crest_1", 0, "Gear", randint(2, 6))
        elif cardType == 'gear-':
            card1 = cardGenerator("card crest_1", randint(20, 100), "Gear", randint(-2, -6))
        else:
            card1 = cardGenerator("Project_1", 0, "Crest", -8,
                                  [randint(-2, 5), randint(-2, 2), randint(-2, 2), randint(-2, 2), randint(-2, 2)],
                                  randint(0, 3))
        drawnCards.append(card1)
    cardChecked = 0
    cardSelection = 0
    for cards in range(0, len(drawnCards)):
        DISPLAYSURF.blit(drawnCards[cardSelection].cardImage, (x, y))
        cardSelection = cardSelection + 1
        x = x + 80
        pygame.display.update()
    x = 520
    while True:
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == MOUSEBUTTONUP:
            for cards in range(0, len(hand)):
                rect = drawnCards[cardChecked].cardImage.get_rect(x=x, y=y)
                if rect.collidepoint(pygame.mouse.get_pos()):
                    print(drawnCards[cardChecked].damage)
                    return drawnCards[cardChecked]
                cardChecked = cardChecked + 1
                x = x + 80
        else:
            continue


enemyHealth = 100
enemyHealthBar = pygame.Rect((100, 100), (enemyHealth, 25))
playerHeathBar = pygame.Rect((100, 100), (playerHealth, 20))
DISPLAYSURF.blit(background, (0, 0))
pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
pygame.display.update()
while start:  # Main loop for the game
    if inCombat:
        pygame.display.update()
        if turn == 0:  # Players turn
            if not drawn:
                playerHealth, currentGears, copper, iron, silver = crestActivator(crests, copper, iron, silver,
                                                                                  playerHealth, currentGears)
                print(playerHealth, currentGears, copper, iron, silver)
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
                if mousey > 885 or mousey < 785:
                    enemyHealth, currentGears = enemyHealth, currentGears
                elif mousex > (len(hand) * 80) + 55 or mousex < 55:
                    enemyHealth, currentGears = enemyHealth, currentGears
                else:
                    enemyHealth, currentGears = playCard(hand[int(getCard())], currentGears, enemyHealth, 1)
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
            print(playerHealth, currentGears, copper, iron, silver)
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
            DISPLAYSURF.blit(ambientBackground, (0, 0))
            pygame.display.update()
            deck.append(randomLootGenerator(3))
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
            enemyHealth, encounter2.currentGears = encounterLoad(encounters[randint(0, 1)])
            hand = []
            discard = []
            drawn = False
            currentGears = 0
            DISPLAYSURF.blit(background, (0, 0))
            pygame.draw.rect(DISPLAYSURF, (255, 0, 0), enemyHealthBar)
            pygame.display.update()
            inCombat = True
