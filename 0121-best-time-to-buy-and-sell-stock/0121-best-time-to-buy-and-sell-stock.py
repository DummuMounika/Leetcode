class Solution(object):
    def maxProfit(self, prices):
        i=1
        max=0
        min= prices[0]
        if len(prices) < 2:
            return 0
        
        while i < len(prices):
            if prices[i] < min:
                min = prices[i]
            else:
                profit = prices[i] - min
                if profit > max:
                    max = profit
            i += 1
        return max