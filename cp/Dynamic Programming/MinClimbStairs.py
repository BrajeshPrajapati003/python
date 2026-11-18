'''
You're climbing 'n' stairs.
You can take 1 or 2 steps at a time.
Return the number of ways to reach the top.
'''

def minClimbStairs(n):
    # return minClimbStairsRecursion(n)
    # dp = [-1]*(n+1)
    # dp[0] = 1; dp[1] = 2
    # return minClimbStairsMemoization(n, dp)
    # return minClimbStairsTabulation(n)
    return minClimbStairsConstantSpace(n)

def minClimbStairsRecursion(n):
    if n <= 2:
        return n
    
    return minClimbStairs(n-1) + minClimbStairs(n-2)

def minClimbStairsMemoization(n, dp):
    if n <= 2:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = minClimbStairsMemoization(n-1, dp) + minClimbStairsMemoization(n-2, dp)
    return dp[n]

def minClimbStairsTabulation(n):
    if n <= 2:
        return n
    
    dp = [0]*(n)
    dp[0] = 1; dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1]

def minClimbStairsConstantSpace(n):
    if n <= 2: 
        return n
    
    prev2, prev1 = 1, 2
    for i in range(2, n):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

n = int(input())
print(minClimbStairs(n))
