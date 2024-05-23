class RandomizedSet(object):

    def __init__(self):
        self.numDict = {}
        self.numList = []
        

    def insert(self, val):
        if val not in self.numDict:
            self.numDict[val] = len(self.numList)
            self.numList.append(val)
            return True
        else:
            return False
            
    def remove(self, val):
        if val in self.numDict:
            last_elementVal = self.numList[-1]
            index = self.numDict[val]
            self.numList[index] = last_elementVal
            self.numList.pop()
            self.numDict[last_elementVal] = index
            del self.numDict[val]
            return True
        else:
            return False
 
    def getRandom(self):
        return choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()