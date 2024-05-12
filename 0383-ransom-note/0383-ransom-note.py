class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dictNote = {}
        if len(ransomNote) > len(magazine):
            return False
        else:
            for char in ransomNote:
                if not dictNote.__contains__(char):
                    dictNote.__setitem__(char,1)
                else:
                    dictNote[char] += 1
            for char in magazine:
                if dictNote.__contains__(char):
                    dictNote[char] -= 1
                    if dictNote[char] == 0:
                        dictNote.pop(char)
                    if not dictNote:
                        return True
            return False
        