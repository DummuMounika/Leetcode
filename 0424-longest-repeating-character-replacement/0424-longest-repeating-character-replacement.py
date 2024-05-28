class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        right = 0
        dictk= {}
        maxlen = 0
        while right < len(s):
            dictk[s[right]] = dictk.get(s[right],0)+1
            currlen = right-left+1
            if currlen - max(dictk.values()) <= k:
                if maxlen < currlen:
                    maxlen = currlen
            else:
                dictk[s[left]] -= 1
                left +=1
            right += 1
        return maxlen



        
                
        