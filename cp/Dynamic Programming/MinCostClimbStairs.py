'''
Given cost[], where cost[i] is the cost of stepping on stair i, reach the top. 
You can start at stair 0 or 1 and climb either 1 or 2 steps. 
Return the minimum total cost.
'''
def minCostClimbStairs(cost):
    # return min(climbRecursion(cost,0), climbRecursion(cost, 1))
    # dp = [-1]*(len(cost))
    # return min(climbMemoization(cost, dp, 0), climbMemoization(cost, dp, 1))
    # return climbTabulation(cost)
    return climbConstantSpace(cost)

def climbRecursion(cost, i):
    if i >= len(cost):
        return 0
    
    oneStep = climbRecursion(cost, i+1)
    twoStep = climbRecursion(cost, i+2)

    return cost[i] + min(oneStep, twoStep)

def climbMemoization(cost, dp, i):
    if i >= len(cost):
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    oneStep = cost[i] + climbMemoization(cost, dp, i+1)
    twoStep = cost[i] + climbMemoization(cost, dp, i+2)

    dp[i] = min(oneStep, twoStep)
    return dp[i]

def climbTabulation(cost):
    if len(cost) <= 1:
        return 0
    
    n = len(cost)
    dp = [0]*n

    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

def climbConstantSpace(cost):
    if len(cost) == 1:
        return 0

    n = len(cost)
    prev2, prev1 = cost[0], cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr
    
    return min(prev1, prev2)

cost = list(map(int, input().split()))
print(minCostClimbStairs(cost))
