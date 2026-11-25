class Sequence:
    def __init__(self, first, prob = 0):
        self.sequence = [first]
        self.probability = prob

    def __str__(self):
        result = ""
        for e in self.sequence:
            result += f"{e} "
        return result

    def __lt__(self, other):
        return self.probability < other.probability

    def getProbability(self):
        return self.probability

    def addWord(self, word, p):
        self.sequence.append(word)
        self.probability = self.probability * p