class Solution(object):
    def isIsomorphic(self, s, t):
            if len(s) != len(t):
                return False
            s_dict = {}
            for i in range(len(s)):
                fir = s[i]
                sec = t[i]
                if fir not in s_dict and sec not in s_dict.values():
                    s_dict.__setitem__(fir,sec)
                elif fir not in s_dict or s_dict[fir] != sec:
                    return False
            return True
        
        