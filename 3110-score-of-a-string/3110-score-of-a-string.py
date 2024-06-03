class Solution(object):
    def scoreOfString(self, s):
        leng = len(s)
        i = 0
        j = 1
        res = 0
        while i < leng and j < leng:
            res += abs(ord(s[i]) - ord(s[j]))
            i += 1   
            j += 1
        return res
            
        
        