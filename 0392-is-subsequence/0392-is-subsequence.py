class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        i=0
        j=0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
                j += 1
            else:
                j+=1   
        return False
        