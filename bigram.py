class Bigram:
    def __init__(self, first, second, prob = 0):
        self.firstWord = first
        self.secondWord = second
        self.probability = prob

    def __str__(self):
        return f"{self.firstWord} {self.secondWord}"

    def __lt__(self, other):
        return self.probability < other.probability

    def getProbability(self):
        return self.probability