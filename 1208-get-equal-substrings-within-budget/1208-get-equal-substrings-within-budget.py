class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        maxlength = 0
        start = 0
        currCost = 0
        for i in range(len(s)):
            currCost += abs(ord(t[i])-ord(s[i]))
            while currCost > maxCost:
                currCost -= abs(ord(t[start]) - ord(s[start]))
                start += 1

            if maxlength < i - start + 1:
                maxlength = i - start + 1
            else:
                maxlength = maxlength

        return maxlength

            



            



            
        
        