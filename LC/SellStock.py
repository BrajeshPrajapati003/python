# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            currProfit = prices[i] - minPrice
            if maxProfit <  currProfit:
                maxProfit = currProfit
            if minPrice > prices[i]:
                minPrice = prices[i]

        return maxProfit
    
