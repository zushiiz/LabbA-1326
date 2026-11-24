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
                    bigram = previousWord + word
                    bigramTable.store(bigram, 1)
                    previousWord = word
    return bigramTable


def main():
    bigrams = findAllBigram()
    while(1):
        u = input(":")
        print(bigrams.search(u))
main()