class Solution(object):
    def wordPattern(self, pattern, s):
        s= s.split(' ')
        dictS = {}
        if len(pattern) != len(s):
            return False
        else:
            for i in range(len(pattern)):
                if not dictS.__contains__(pattern[i]) and s[i] not in dictS.values():
                    dictS.__setitem__(pattern[i],s[i])
                elif not dictS.__contains__(pattern[i]) or dictS[pattern[i]] != s[i]:
                    return False
            return True