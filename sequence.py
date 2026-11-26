"""
Written by Zixuan Huang (zixuanhu@ug.kth.se) No use of AI
Created 2026-11-25
"""
class Sequence:
    def __init__(self, seq = [], prob = 0):
        self.sequence = []
        for e in seq:
            self.sequence.append(e)
        self.lastWord = self.sequence[len(self.sequence)-1]
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

    def getSequence(self):
        return self.sequence

    def addWord(self, word, p):
        self.sequence.append(word)
        self.probability = self.probability * p