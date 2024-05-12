class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        start=strs[0]
        end=strs[-1]
        res = ''
        for i in range(len(start)):
            if start[i] == end[i]:
                res += start[i]
            else:
                break
        return res
        