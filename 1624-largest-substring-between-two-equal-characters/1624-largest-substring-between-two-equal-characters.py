class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        dicts= {}
        ans = -1
        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = i
            else:
                if ans < i - dicts[s[i]] - 1:
                    ans = i - dicts[s[i]] - 1
        return ans
                
            
                

        