# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        for i in range(n-1):
            currProfit = prices[i+1] - prices[i]
            if currProfit > 0:
                maxProfit += currProfit
        return maxProfit
    
