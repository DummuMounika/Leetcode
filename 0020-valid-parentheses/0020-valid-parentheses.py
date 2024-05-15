class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sdict = {'(':')', '{':'}','[':']'}
        stack = []
        for c in s:
            if c in sdict:
                stack.append(c)
            elif len(stack) == 0 or sdict[stack.pop()] != c:
                return False
        return len(stack) == 0

                 


        
    
    
    
        