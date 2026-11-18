'''
You are given:
height[] — height of each stone, K — max distance you can jump.
You start at stone 0 and need to reach stone n-1.
You can jump forward by 1 to K stones.
The energy required for a jump from stone i to stone j is:
    |height[i]-height[j]|
Find the minimum total energy.
'''
def frog2(height, k):
    # return frog2Recursion(height, k, len(height)-1)
    # dp = [-1]*len(height)
    # return frog2Memoization(height, k, dp, len(height)-1)
    # return frog2Tabulation(height, k)
    return frog2UsingKSpace(height, k)

def frog2Recursion(height, k, i):
    if i == 0:
        return 0
    
    minEnergy = float('inf')

    for j in range(1, min(i, k)+1):
        curr = frog2Recursion(height, k, i-j) + abs(height[i]-height[i-j])
        minEnergy = min(curr, minEnergy)
    
    return minEnergy

def frog2Memoization(height, k, dp, i):
    if i == 0:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    minEnergy = float('inf')
    for j in range(1, min(i, k)+1):
        curr = frog2Memoization(height, k, dp, i-j) + abs(height[i]-height[i-j])
        minEnergy = min(curr, minEnergy)

    dp[i] = minEnergy
    return dp[i]

def frog2Tabulation(height, k):
    n = len(height)
    if n <= 1:
        return 0
    
    dp = [0]*n
    dp[0] = 0

    for i in range(1, n):
        minEnergy = float('inf')
        for j in range(1, min(i, k)+1):
            curr = dp[i-j] + abs(height[i]-height[i-j])
            minEnergy = min(curr, minEnergy)
        
        dp[i] = minEnergy
    
    return dp[n-1]

def frog2UsingKSpace(height, k):
    n = len(height)
    if n <= 1:
        return 0
    
    dp = [0]*k
    
    for i in range(1, n):
        minEnergy = float('inf')
        for j in range(1, min(i, k)+1):
            curr = dp[(i-j)%k] + abs(height[i]-height[i-j])
            minEnergy = min(curr, minEnergy)
        
        dp[i%k] = minEnergy

    return dp[(n-1)%k]

height = list(map(int, input().split()))
k = int(input())
print(frog2(height, k))
