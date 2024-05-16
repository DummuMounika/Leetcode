class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimumStack = []
        

    def push(self, val):
        self.stack.append(val)
        if len(self.minimumStack) == 0:
            self.minimumStack.append(val)
        elif (val < self.minimumStack[-1]):
            self.minimumStack.append(val)
        else:
            self.minimumStack.append(self.minimumStack[-1]) 



    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            self.minimumStack.pop()
            result = self.stack.pop()
            return  result
           

    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        

    def getMin(self):
        if not self.stack:
            return -1
        else:
            return self.minimumStack[-1]
            

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()