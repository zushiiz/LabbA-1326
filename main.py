"""
Written by Zixuan Huang (zixuanhu@ug.kth.se) No use of AI
Created 2026-11-24
"""
from hashtable import Hashtable

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

def nextWord(searchedWord, hashtable):
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
    return nextWord


def main():
    bigrams = findAllBigram()
    while(1):
        u = input(":")
        print(f"Result {nextWord(u, bigrams)}")

main()