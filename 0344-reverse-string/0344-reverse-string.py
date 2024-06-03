class Solution(object):
    def reverseString(self, s):
        leng = len(s)
        i = 0
        j = leng-1
        while i < j:
            temp1 = s[i]
            s[i] = s[j]
            s[j] = temp1
            i += 1
            j -= 1
        return s
            
            