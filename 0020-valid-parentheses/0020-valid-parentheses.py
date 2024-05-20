class Solution(object):
    def isValid(self, s):
        
        
        dictS = { '(': ')', '{': '}','[': ']' }    
        
        stack = []
        
        for char in s:
            if char in dictS:
                stack.append(dictS[char])
                
            else:
                if len(stack) != 0 and char == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
            
        
        