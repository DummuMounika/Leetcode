class Solution(object):
    def maxProfit(self, prices):
        days=len(prices)
        i=1
        maxP = 0
        minP = prices[0]
        temp = 0
        if days < 2:
            return 0
        while i < days:
            if prices[i] < minP:
                minP = prices[i]
            else:
                profit =prices[i]-minP
                if profit > maxP:
                    maxP = profit
                    temp += profit
                    minP = prices[i]
                    maxP = 0
            i += 1
        return temp
        