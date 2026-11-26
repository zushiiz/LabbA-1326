"""
Written by Zixuan Huang (zixuanhu@ug.kth.se) No use of AI
Created 2026-11-24
"""
from hashtable import Hashtable
from sequence import Sequence
from linkedQFile import LinkedQ
from heapQueue import PriorityQueue

class Bigram:
    def __init__(self, bigram, prob):
        t = bigram.split("|")
        self.first = t[0]
        self.last = t[1]
        self.prob = prob
    def __lt__(self, other):
        return self.prob < other.prob
    def getLast(self):
        return self.last
    def getProbability(self):
        return self.prob

def findAllBigram():
    bigramTable = Hashtable(77000 + 77000)
    previousWord = ""
    with open("acd_alla.txt", "r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip().split()         
            if len(line) == 0:
                previousWord = ""
            for word in line:
                word = "".join(char.lower() for char in word if char.isalnum()) # Removes special characters
                if previousWord == "":
                    previousWord = word
                else:
                    bigram = f"{previousWord}|{word}"
                    bigramTable.store(bigram, 1)
                    previousWord = word
    bigramTable.filterData(1) # Rids of all bigrams appearing once
    return bigramTable

def highestProbableNextWord(searchedWord, hashtable):
    searchedWord = searchedWord.lower()
    bigrams = set()
    totalAppearence = 0
    for node in hashtable.slots:
        if node != None and node is not hashtable.tombstone:
            splitBigram = node.key.split("|")
            if searchedWord == splitBigram[0]:
                totalAppearence += node.data
                bigrams.add(node.key)

    prevProb = 0
    for bigram in bigrams:
        print(bigram)
        prob = hashtable.search(bigram) / totalAppearence
        if prevProb < prob:
            nextWord = bigram
        print(f"{bigram} prob:{prob}%")
        prevProb = prob
    return nextWord, prob

def findAllSpecificBigram(firstWord, hashtable):
    bigrams = set()
    totalAppearence = 0
    for node in hashtable.slots:
        if node != None and node is not hashtable.tombstone:
            splitBigram = node.key.split("|")
            if firstWord == splitBigram[0]:
                bigrams.add(node.key)
                totalAppearence += node.data
    return bigrams, totalAppearence

def bigramProbabilityCalc(bigram, total, hashtable):
    return hashtable.search(bigram) / total

def beamSearch(startWord, n, b):
    bigramsHash = findAllBigram()
    finalSequences = PriorityQueue("max")
    q = LinkedQ()
    startSequence = Sequence([startWord])
    q.enqueue(startSequence)
    for i in range(n-b):
        seq = q.dequeue()
        makeChildren(seq, q, b, bigramsHash)

    while q.isEmpty() != False:
        finalSequences.enqueue(q.dequeue)

    print(finalSequences.size())
    for i in range(finalSequences.size()):
        print(finalSequences.dequeue())

def makeChildren(sequence, q, b, bigramsHash):
    word = sequence.lastWord
    bigrams, firstWordAmount = findAllSpecificBigram(word, bigramsHash)

    allBigramChildren = PriorityQueue("max")
    for bigram in bigrams:
        bigramProb = bigramProbabilityCalc(bigram, firstWordAmount, bigramsHash)
        allBigramChildren.enqueue(Bigram(bigram, bigramProb))
    for i in range(b):
        newSequence = Sequence(sequence.getSequence())
        newWord = allBigramChildren.dequeue()
        newSequence.addWord(newWord.getLast(), newWord.getProbability())
        q.enqueue(newSequence)
        

    # allBigramChildren = PriorityQueue("max")
    # for bigram in bigrams:
    #     allChildren.enqueue(Sequence(bigram, bigramProbabilityCalc(bigram, startWordAmount, bigramsHash)))
    # for i in range(b):
    #     q.enqueue(allChildren.dequeue)
    # return True


def main():
    beamSearch("sherlock", 5, 2)
main()