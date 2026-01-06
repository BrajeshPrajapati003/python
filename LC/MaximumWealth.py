# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     maxWealth = 0
    #     m = len(accounts)
    #     n = len(accounts[0])
    #     for i in range(m):
    #         currSum = 0
    #         for j in range(n):
    #             currSum += accounts[i][j]
    #             if maxWealth < currSum:
    #                 maxWealth = currSum
    #         currSum = 0
    #     return maxWealth
    

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            maxWealth = max(maxWealth, sum(account))
        return maxWealth
    
