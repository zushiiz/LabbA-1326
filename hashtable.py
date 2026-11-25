"""
Copied code from Labb 7
Original written by Zixuan Huang and Simon Ek De Bernardo
Modified by Zixuan Huang (zixuanhu@ug.kth.se) No use of AI
Added 2026-11-24
"""

class HashNode:
    def __init__(self, key = None, data = None):
      """key är nyckeln som anvands vid hashningen
         data är det objekt som ska hashas in"""
      self.key = key
      self.data = data

class Tombstone: #https://en.wikipedia.org/wiki/Lazy_deletion
   def __init__(self):
      pass

class Hashtable:
   def __init__(self, size):
      """size: hashtabellens storlek"""
      self.size = size #Amount of data
      self.slots = [None] * self.size*2 #Two times more slots than amount of data
      self.tombstone = Tombstone()

   def store(self, key, data):
      counter = 0
      hashedKey = self.hashfunction(key)
      tombstoneIndex = None
      while self.slots[hashedKey] != None:
         if self.slots[hashedKey] is self.tombstone and tombstoneIndex == None: # Added Tombstone check
            tombstoneIndex = hashedKey

         if self.slots[hashedKey] is not self.tombstone:
            if self.slots[hashedKey].key == key:
               self.slots[hashedKey].data += data # Ändrad för labb A, lägger till en instans av ett bigram
               return True
            
         if (self.size*2) <= counter and tombstoneIndex == None: #2x size?
            print("Det finns inte plats för noden i hashtabellen")
            return False
         
         hashedKey = (hashedKey+1)%(len(self.slots))
         counter += 1

      if tombstoneIndex == None:
         self.slots[hashedKey] = HashNode(key, data)
      else:
         self.slots[tombstoneIndex] = HashNode(key, data)
      return True
   
   def search(self, key):
      hashedKey = self.hashfunction(key)
      while self.slots[hashedKey] != None:
         if self.slots[hashedKey] is not self.tombstone:
            if self.slots[hashedKey].key == key:
               return self.slots[hashedKey].data
            hashedKey = (hashedKey+1)%(len(self.slots))    
         else:
            hashedKey = (hashedKey+1)%(len(self.slots))            
            continue
      raise KeyError
      
   def hashfunction(self, key):
      #firstChar*lastChar * stringLength (mod hashTableSize)
      temp = 0
      for char in key:
         temp = (temp + ord(char)*ord(char))*64    
      hashedKey = temp%(len(self.slots))
      return int(hashedKey)
   
   def _createTombstone(self, index):
      self.slots[index] = self.tombstone

   def filterData(self, n):
      for i in range(self.size*2):
         if self.slots[i] is not self.tombstone and self.slots[i] != None and self.slots[i].data == n:
            self._createTombstone(i)