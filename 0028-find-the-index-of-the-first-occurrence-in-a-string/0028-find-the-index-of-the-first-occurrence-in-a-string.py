class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if needle == haystack[i:i+len(needle)]:
                    return i
        