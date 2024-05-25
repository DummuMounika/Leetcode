class Solution(object):
    def maxScore(self, cardPoints, k):
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        res = total
        print(res)

        while right < len(cardPoints):
            total += cardPoints[left] - cardPoints[right]
            res = max(res, total)
            left += 1
            right += 1
        return res

        

        



        