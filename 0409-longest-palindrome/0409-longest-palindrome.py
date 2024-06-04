class Solution(object):
    def longestPalindrome(self, s):
        dictS = {}
        res = 0
        oddres = 0
        for i in range(len(s)):
            if not s[i] in dictS:
                dictS[s[i]] = 1
            else:
                val = 1
                dictS[s[i]] += val
        for val in dictS.values():
            res += val
            if val % 2 != 0:
                oddres += 1
        if oddres != 0:
            return res - oddres + 1
        elif oddres == 0:
            return res - oddres
                
            
        