'''
A frog is at idx 0. It wants to reach idx n-1.
It can jump: 1 or 2 steps.
Each idx has a height.
    cost = absolute difference of heights
Find min. cost to reach end.
'''
def frog1(height):
    # return frogRecursion(height, 0)
    # dp = [-1]*len(height)
    # return frogMemoization(height, dp, 0)
    # return frogTabulation(height)
    return frogConstantSpace(height)

def frogRecursion(height, i):
    n = len(height)
    if i == n-1:
        return 0
    
    jump1 = frogRecursion(height, i+1) + abs(height[i]-height[i+1])
    jump2 = float('inf')
    if i+2 < n:
        jump2 = frogRecursion(height, i+2) + abs(height[i]-height[i+2])

    return min(jump1, jump2)

def frogMemoization(height, dp, i):
    n = len(height)
    if i == n-1:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    jump1 = frogMemoization(height, dp, i+1) + abs(height[i]-height[i+1])
    jump2 = float('inf')
    if i+2 < n:
        jump2 = frogMemoization(height, dp, i+2) + abs(height[i]-height[i+2])
    
    dp[i] = min(jump1, jump2)
    return dp[i]

def frogTabulation(height):
    if len(height) == 1:
        return 0
    
    n = len(height)
    dp = [0]*n
    dp[0] = 0; dp[1] = abs(height[1]-height[0])
    for i in range(2, n):
        jump1 = dp[i-1] + abs(height[i]-height[i-1])
        jump2 = dp[i-2] + abs(height[i]-height[i-2])
        dp[i] = min(jump1, jump2)
    
    return dp[n-1]

def frogConstantSpace(height):
    if len(height) == 1:
        return 0

    prev2 = 0; prev1 = abs(height[1]-height[0])
    for i in range(2, len(height)):
        jump1 = prev1 + abs(height[i]-height[i-1])
        jump2 = prev2 + abs(height[i]-height[i-2])
        
        prev2 = prev1
        prev1 = min(jump1, jump2)

    return prev1

height = list(map(int, input().split()))
print(frog1(height))
