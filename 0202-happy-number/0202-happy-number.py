class Solution(object):
    def isHappy(self, n):
        dictnumb= {}
        while n > 0:
            sq = 0
            while n > 0:
                rem = n % 10
                sq += rem ** 2
                n = n // 10
            n = sq
            if dictnumb.__contains__(sq):
                res=dictnumb.get(sq) + 1
                dictnumb.__setitem__(sq, res)
                return False
            else:
                dictnumb.__setitem__(sq,1)
            if sq == 1:
                return True
        return False
        