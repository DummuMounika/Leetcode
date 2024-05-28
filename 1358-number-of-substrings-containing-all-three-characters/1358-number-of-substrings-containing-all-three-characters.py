class Solution(object):
    def numberOfSubstrings(self, s):
        dictS = {}
        totalsubarrays = 0
        start = 0
        end = 0
        n = len(s)
        while end < n:
            dictS[s[end]] = dictS.get(s[end],0) + 1
            while dictS.get('a', 0) > 0 and dictS.get('b', 0) >0 and dictS.get('c', 0) > 0:
                totalsubarrays += n - end
                dictS[s[start]] -= 1
                start += 1
            end += 1
        return totalsubarrays
                
            
        
        