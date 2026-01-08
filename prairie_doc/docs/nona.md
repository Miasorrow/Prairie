# JEUX
## I- main.py
```py
La boucle qui permet de lancer les parties plusieurs fois et tester les stratégies

from partie import partie
from strategies import rand, plusGrande, plusPetite, smart

n_parties = 10_000
victoires_robot = 0
for i in range(n_parties):
    gagnant = partie(
        strategy_humain=smart,
        strategy_robot=smart)
    if gagnant.name == "Robot":
        victoires_robot += 1

print("% victoire robot: ", victoires_robot / n_parties)
```
# II- Player

C'est la classe qui a la liste de la main du joueur ainsi que la classe play avec les stratégies qu'on implémente dans notre algo

```py
class Player:
    def __init__(self, name: str, strategy):
        self.name = name
        self.hand = []
        self.strategy = strategy

    def __str__(self):
        return self.name + ": " + str([str(c) for c in self.hand])

    def play(self, carte=None):
        return self.strategy(self.hand, carte)
```


# III- card

C'est la classe card celle qui contient la valeur et la forme

```py
class Card:
    def __init__(self, value: int, shape: str):
        self.value = value
        self.shape = shape

    def getValue(self):
        return self.value

    def __str__(self):
        return self.shape + str(self.value)
```
# IV - partie

L'algo pour faire une partie 
```py
import random

from Card import Card
from player import Player
from strategies import rand


def partie(strategy_humain, strategy_robot):
    # les cartes
    pioche = [
        Card(0, "R"),
        Card(1, "R"),
        Card(2, "R"),
        Card(3, "R"),
        Card(4, "R"),
        Card(1, "C"),
        Card(2, "C"),
        Card(3, "C"),
        Card(4, "C"),
        Card(5, "C"),
    ]
    # les joueurs
    humain = Player("Humain", strategy_humain)
    robot = Player("Robot", strategy_robot)
    # mélange
    random.shuffle(pioche)
    # distribution
    while len(pioche) > 0:
        carte = pioche.pop(-1)
        humain.hand.append(carte)
        carte = pioche.pop(-1)
        robot.hand.append(carte)

    # tours
    points_du_robot = 0
    for tour in range(5):
        carte_du_robot = robot.play()
        carte_de_humain = humain.play(carte_du_robot)
        if carte_du_robot.value >= carte_de_humain.value:
            points_du_robot += 1
    # victoire
    if points_du_robot >= 3:
        return robot
    else:
        return humain
```

# V - strategies

Les différentes "stratégies"

```py
import random
from Card import Card

def rand(hand, carte):
    random.shuffle(hand)
    return hand.pop()


def plusGrande(hand, carte):
    hand.sort(key=lambda carte: carte.value)
    return hand.pop(-1)

def plusPetite(hand, carte):
    hand.sort(key=lambda carte: carte.value)
    return hand.pop()

def smart(hand, carte):
    if carte:
        hand.sort(key=lambda c: c.value)
        for c in hand:
            if c.value > carte.value:
                hand.remove(c)
                return c
    return plusPetite(hand, carte)
```