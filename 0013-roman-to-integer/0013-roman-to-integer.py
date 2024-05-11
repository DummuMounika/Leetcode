class Solution(object):
    def romanToInt(self, s):
        res=0
        symDict = {'I': 1,'IV': 4,'V':5,'IX': 9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        for i in range(len(s)):
            if i < len(s)-1 and symDict.get(s[i]) < symDict.get(s[i+1]):
                res -= symDict.get(s[i])
            else:
                res += symDict.get(s[i])
        return res
        