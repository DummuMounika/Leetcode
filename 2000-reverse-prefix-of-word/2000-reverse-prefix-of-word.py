class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        f= word.find(ch)
        while f!=-1:
            return word[:f+1][::-1]+ word[f+1:]
        return word
        