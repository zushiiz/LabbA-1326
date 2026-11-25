"""
Copied code from Labb 4
Original written by Zixuan Huang and Simon Ek De Bernardo
Modified by Zixuan Huang (zixuanhu@ug.kth.se) No use of AI
Added 2026-11-24
"""
class Node:
    def __init__(self, value):
        self.key = value
        self.rightPointer = None
        self.leftPointer = None

    def __str__(self):
        return "Jag är " + self.key

class Bintree:
    def __init__(self):
        self.root = None

    def put(self, value):
        if self.__contains__(value) == False:  
            t = pushNode(self.root, value)
            if t == None:
                pass
            else:
                self.root = t
        else:
            print("Existerar redan")

    def __contains__(self, value):
        return finns(self.root, value)

    def write(self):
        skriv(self.root)
    
        print("\n")

def pushNode(parent, value):
    if parent == None:
        return Node(value)
    else:
        if max(parent.key, value) == parent.key:
            if parent.leftPointer:
                pushNode(parent.leftPointer, value)
            else:
                parent.leftPointer = Node(value)
        elif min(parent.key, value) == parent.key:
            if parent.rightPointer:
                pushNode(parent.rightPointer, value)
            else:
                parent.rightPointer = Node(value)

def finns(p,value):
    stringValue = str(value)
    if p == None:
        return False

    if p.key == stringValue:
        return True    
      
    if min(p.key, stringValue) == stringValue:
        return finns(p.leftPointer, value)
    return finns(p.rightPointer, value)

def skriv(p):
     # Funktion som gör själva jobbet att skriva ut trädet
    if p.leftPointer != None:
         skriv(p.leftPointer)     
    print(p)
    if p.rightPointer != None:
        skriv(p.rightPointer)    
