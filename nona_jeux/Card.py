# card.py

class Card:
    def __init__(self, value: int, shape: str):
        self.value = value
        self.shape = shape

    def getValue(self):
        return self.value

    def __str__(self):
        return self.shape + str(self.value)