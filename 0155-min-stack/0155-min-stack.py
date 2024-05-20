class MinStack(object):
    
    class Node:
        def __init__(self,val,next,min_val):
            self.val = val
            self.next = next
            self.min_val = min_val

    def __init__(self):
        self.head = None
        
    def push(self, val):
        if self.head is None:
            self.head = self.Node(val,None,val)
        else:
            self.head = self.Node(val, self.head, min(val, self.head.min_val))
        
        
    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        # else:
        #     raise IndexError("Stack is empty")
        
        
    def top(self):
        if self.head is not None:
            return self.head.val
        #raise IndexError("Stack is empty")
        
    def getMin(self):
        if self.head is not None:
            return self.head.min_val
        #raise IndexError("Stack is empty")
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()