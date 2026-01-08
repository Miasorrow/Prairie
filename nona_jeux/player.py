class Player:
    def __init__(self, name: str, strategy):
        self.name = name
        self.hand = []
        self.strategy = strategy

    def __str__(self):
        return self.name + ": " + str([str(c) for c in self.hand])

    def play(self, carte=None):
        return self.strategy(self.hand, carte)
    

