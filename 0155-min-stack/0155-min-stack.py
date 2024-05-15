class MinStack(object):

    def __init__(self):
        self.minStack = []
        

    def push(self, val):
        self.minStack.append(val)
        

    def pop(self):
        if not self.minStack:
            return -1
        else:
            return self.minStack.pop()


        

    def top(self):
        if not self.minStack:
            return -1
        else:
            return self.minStack[-1]
        

    def getMin(self):
        if not self.minStack:
            return -1
        else:
            return min(self.minStack)

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()