class Solution(object):
    def reverseWords(self, s):
        slist=s.split()
        res = ''
        for c in range(len(slist)-1,-1,-1):
                res += slist[c]
                if c != 0:
                    res += " "
        return res
        