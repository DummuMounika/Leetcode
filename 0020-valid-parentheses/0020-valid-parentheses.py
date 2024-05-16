class Solution(object):
    
    def isValid(self, s):

        stack = []
        for i in range(len(s)):
            ch = s[i]
            if (ch == '(' or ch == '{' or ch == '['):
                stack.append(ch)
            else:
                if len(stack) == 0: 
                    return False
                if ((stack[-1] == '(' and ch == ')') or (stack[-1] == '{' and ch == '}') 
                or (stack[-1] == '[' and ch == ']')):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

                 


        
    
    
    
        