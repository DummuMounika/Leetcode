class Solution(object):
    def lengthOfLongestSubstring(self, s):
        setCh= set()
        j= 0
        lengR= 0
        for c in range(len(s)):
            while s[c] in setCh:
                setCh.remove(s[j])
                j+=1
            setCh.add(s[c])
            temp= c-j+1
            if temp > lengR:
                lengR=temp
        return lengR

        
        