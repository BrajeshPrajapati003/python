'''
The houses are arranged in a circle instead of a straight line.
You cannot rob two adjacent houses. Since the houses are circular, the first and last houses are also adjacent.
Given nums, return the maximum money you can rob.
'''
def houseRobber2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n==2:
        return max(nums[0], nums[1])
    
    # return max(houseRobber2Recursion(nums, 0, n-2), 
    #     houseRobber2Recursion(nums, 1, n-1))

    # dp1 = [-1]*n; dp2 = [-1]*n
    # case1 = houseRobber2Memoization(nums, 0, n-2, dp1)
    # case2 = houseRobber2Memoization(nums, 1, n-1, dp2)
    # return max(case1, case2)

    # return houseRobber2Tabulation(nums)
    return houseRobber2ConstantSpace(nums)

def houseRobber2Recursion(nums, start, i):
    if i<start:
        return 0
    if i==start:
        return nums[start]
    
    pick = nums[i] + houseRobber2Recursion(nums, start, i-2)
    skip = houseRobber2Recursion(nums, start, i-1)

    return max(pick, skip)

def houseRobber2Memoization(nums, start, i, dp):
    if i < start:
        return 0
    if i==start:
        return nums[start]
    
    if dp[i] != -1:
        return dp[i]
    
    pick = nums[i] + houseRobber2Memoization(nums, start, i-2, dp)
    skip = houseRobber2Memoization(nums, start, i-1, dp)
    dp[i] = max(pick, skip)
    return dp[i]

def houseRobber2Tabulation(nums):
    n = len(nums)

    dp1 = [0]*(n)
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    for i in range(2, n-1):
        pick = nums[i] + dp1[i-2]
        skip = dp1[i-1]

        dp1[i] = max(pick, skip)

    dp2 = [0]*(n)
    dp2[1] = nums[1]
    dp2[2] = max(nums[1], nums[2])
    for i in range(3, n):
        pick = nums[i] + dp2[i-2]
        skip = dp2[i-1]
        
        dp2[i] = max(pick, skip)
    
    return max(dp1[n-2], dp2[n-1])

def houseRobber2ConstantSpace(nums):
    n = len(nums)
    
    prevA2, prevA1 = nums[0], max(nums[0], nums[1])
    for i in range(2, n-1):
        pick = nums[i] + prevA2
        skip = prevA1

        prevA2 = prevA1
        prevA1 = max(pick, skip)

    prevB2, prevB1 = nums[1], max(nums[1], nums[2])
    for i in range(3, n):
        pick = nums[i] + prevB2
        skip = prevB1

        prevB2 = prevB1
        prevB1 = max(skip, pick)
    
    return max(prevA1, prevB1)

nums = list(map(int, input().split()))
print(houseRobber2(nums))
