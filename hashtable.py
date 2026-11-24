class HashNode:
    def __init__(self, key = None, data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data

class Hashtable:
   def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size #Amount of data
      self.slots = [None] * self.size*2 #Two times more slots than amount of data

   def store(self, key, data):
      counter = 0
      hashedKey = self.hashfunction(key)
      
      while self.slots[hashedKey] != None:

         if self.slots[hashedKey].key == key:
            self.slots[hashedKey].data += data # Ändrad för labb A, lägger till en instans av ett bigram
            return True

         if self.size == counter:
            print("Det finns inte plats för noden i hashtabellen")
            return False
         
         hashedKey += 1
         hashedKey = hashedKey%(len(self.slots))
         counter += 1
      self.slots[hashedKey] = HashNode(key, data)
      return True
   
   def search(self, key):
      hashedKey= self.hashfunction(key)
      while self.slots[hashedKey] != None:
         if self.slots[hashedKey].key == key:
            return self.slots[hashedKey].data
         hashedKey += 1
         hashedKey = hashedKey%(len(self.slots))
      raise KeyError
      
   def hashfunction(self, key):
      #firstChar*lastChar * stringLength (mod hashTableSize)
      temp = 0
      for char in key:
         temp = (temp + ord(char)*ord(char))*64    
      hashedKey = temp%(len(self.slots))
      return int(hashedKey)