class Solution(object):
    def isPalindrome(self, s):
        l=""
        for char in s:
            if 'A' <= char <='Z': #for conversion into lowercase
                char= chr(ord(char)+32)
                l+=char
            else:
                if 'a' <= char <= 'z' or '0' <= char <= '9':
                    l+=char
        i=0
        leng= len(l)
        while i < leng:
            if l[i] != l[leng - i - 1]:
                return False
            i+=1
        return True
        