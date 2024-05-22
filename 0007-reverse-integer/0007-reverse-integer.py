class Solution(object):
    def reverse(self, x):
        minX = -2**31
        maxX = 2**31 - 1 
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        revX = int(str(x)[::-1])
        if revX >= maxX or revX <= minX:
            return 0
        return revX*sign
            
        