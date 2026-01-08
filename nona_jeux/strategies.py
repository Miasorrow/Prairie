# strategies
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