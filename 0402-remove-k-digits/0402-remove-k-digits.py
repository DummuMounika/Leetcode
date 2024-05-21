class Solution(object):
    def removeKdigits(self, num, k):
        if k == 0:
            return nums
        elif k == len(num):
            return '0'

        stack = [] #Intitalize a empty string
        for digit in num: 
            while k > 0 and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k>0 and stack:
            stack.pop()
            k -= 1

        temp =''
        for i in stack:
            temp+=i

        temp = int(temp)
        return str(temp)

        
        