class MyQueue(object):

    def __init__(self):
        self.inputQueue = []
        self.outputStack = []
        

    def push(self, x):
        self.inputQueue.append(x)
        

    def pop(self):
        if not self.outputStack:
            while self.inputQueue:
                self.outputStack.append(self.inputQueue.pop())
        return self.outputStack.pop()    
         

    def peek(self):
        if not self.outputStack:
            while self.inputQueue:
                self.outputStack.append(self.inputQueue.pop())
        return self.outputStack[-1]

    def empty(self):
        if not self.outputStack and not self.inputQueue:
            return True
        else:
            return False
            
            

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()