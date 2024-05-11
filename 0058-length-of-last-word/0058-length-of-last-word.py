class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in range(len(s)-1,-1,-1):#time compexity O(n)
            if s[i] == ' ':
                if count != 0:
                    return count
                continue
            else:
                count += 1
        return count
        