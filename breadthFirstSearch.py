from bintreeFile import Bintree
from linkedQFile import LinkedQ


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
        
    def __str__(self):
        return self.word

def createBinTree(wordList):
    with open("Labb 3/word3.txt", "r", encoding = "utf-8") as sweFile:
        for rad in sweFile:
            word = rad.strip()           
            if word in wordList:
                pass
            else:
                wordList.put(word)   

def main():
    wordList = Bintree()
    oldList = Bintree()
    createBinTree(wordList)
    userInput = input("Skriv in dit startord, slutord:\n").strip().split(",")
    q = LinkedQ()
    firstNode = ParentNode(userInput[0])

    q.enqueue(firstNode)
    while not q.isEmpty():
        node = q.dequeue()
        makeChildrenSuccess, lastNode = makeChildren(node, userInput[1].strip(), wordList, oldList, q)
        if makeChildrenSuccess == False:
            break
        
    if isPossible(userInput[1], oldList):
        # print(f"Det finns en relation från ordet:{userInput[0]} till {userInput[1]}")
        writeChain(lastNode)
    else:
        print("Det finns ingen relation mellan orden")

def makeChildren(startNode, endWord, wordList, oldList, q):
    startWord = startNode.word

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","å","ä","ö"]
    for i in range(len(startWord)):
        for char in alphabet:

            tempWord = startWord.replace(startWord[i], char)
            tempNode = ParentNode(tempWord, startNode)
            if tempWord == endWord and tempWord in wordList:
                #print(f"Det finns en väg mellan orden {tempWord} och {endWord}")
                oldList.put(tempWord)
                return False, tempNode
            
            if tempWord in wordList and tempWord != startWord:

                if (tempWord in oldList) == False: 
                    q.enqueue(tempNode)
                    oldList.put(tempWord)
        i += 1
    return True, None
    
    

def isPossible(endWord, oldList):
    if endWord.strip() in oldList:
        return True
    else:
        return False

def writeChain(node):
    if node.parent == None:
        print(node)
        return
    writeChain(node.parent)
    print(node)

        
main()