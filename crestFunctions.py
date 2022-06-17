class crest:
    def __init__(self, nam, effects, spot):
        self.name = nam
        self.effects = effects  # List order, health, gears, copper, iron, silver
        self.crestSpot = spot
        print(self.name, 'constructed')


placeholder = None


class card:  # All the cards info is stored here
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    cardImage = placeholder
    damage = 0
    gearCost = 0
    cardType = "Placeholder"
    weight = 0
    crestEffects = "none"


def crestActivator(crests, copper, iron, silver, health, gears):
    activatedCrest = 0
    currentStats = [health, gears, copper, iron, silver]
    for length in range(0, len(crests)):
        available = True
        if len(crests) == activatedCrest:
            return currentStats
        if crests[activatedCrest] == 'none':
            activatedCrest += 1
            continue
        effectCheck = 0
        crestEffects = crests[activatedCrest].effects
        for effects in range(0, 5):
            effectCheck += 1
            if crestEffects[effectCheck - 1] == 0:
                continue
            elif crestEffects[effectCheck - 1] < 0:
                if (currentStats[effectCheck - 1] + crestEffects[effectCheck - 1]) < 0:
                    available = False
                    break
            else:
                continue
        if available:
            changed = 0
            for effects in range(0, 5):
                currentStats[changed] = currentStats[changed] + crestEffects[changed]
                changed += 1
        activatedCrest += 1
    health, gears, copper, iron, silver = currentStats
    return health, gears, copper, iron, silver


def cardGenerator(name, damage, type, gearCost, effects=None, spot=0):  # makes a new card
    if effects is None:
        effects = []
    name = card(name)
    name.damage = damage
    name.cardType = type
    name.cardImage = None
    if type.lower() == "gear":
        name.gearCost = gearCost
        return name
    if type.lower() == "crest":
        name.crestEffects = crest(name, effects, spot)
    return name


def main():
    crest1 = cardGenerator("Project_1", 0, "Crest", -8, [5, -1, 0, 0, 0], 0)
    crest2 = cardGenerator("Project_1", 0, "Crest", -8, [0, 1, -1, 0, 0], 1)
    crests = [crest1, crest2, 'none', 'none']
    health, gears, copper, iron, silver = 50, 5, 0, 0, 0
    print(crestActivator(crests, copper, iron, silver, health, gears))


if __name__ == "__main__":
    main()
