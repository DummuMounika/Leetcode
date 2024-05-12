class Solution(object):
    def wordPattern(self, pattern, s):
        s= s.split(' ')
        print(s)
        dictS = {}
        # dictPattern = {}
        if len(pattern) != len(s):
            return False
        # else:
        #     for i in range(len(pattern)):
        #         if dictS.__contains__(pattern[i]) and dictS.get(pattern[i]) != s[i]:
        #             return False
        #         if dictPattern.__contains__(s[i]) and dictPattern.get(s[i]) != pattern[i]:
        #             return False
        #         dictS.__setitem__(pattern[i],s[i])
        #         dictPattern.__setitem__(s[i],pattern[i])
        #     return True
        else:
            for i in range(len(pattern)):
                if not dictS.__contains__(pattern[i]) and s[i] not in dictS.values():
                    dictS.__setitem__(pattern[i],s[i])
                elif not dictS.__contains__(pattern[i]) or dictS[pattern[i]] != s[i]:
                    return False
            return True