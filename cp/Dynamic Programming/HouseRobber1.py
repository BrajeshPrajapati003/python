'''
You are a robber planning to rob houses arranged in a row.
Each house has some money. The restriction is:
    You cannot rob two adjacent houses.
Given an array nums, return the maximum amount of money you can rob without triggering the alarm.
'''
def houseRobber(nums):
    # return houseRobberRecursion(nums, len(nums)-1)
    # dp = [-1]*len(nums)
    # return houseRobberMemoization(nums, dp, len(nums)-1)
    # return houseRobberTabulation(nums)
    return houseRobberConstantSpace(nums)

def houseRobberRecursion(nums, n):
    if n == 0:
        return nums[0]
    
    if n < 0:
        return 0
    
    pick = houseRobberRecursion(nums, n-2) + nums[n]
    skip = houseRobberRecursion(nums, n-1)
    return max(pick, skip)

def houseRobberMemoization(nums, dp, i):
    if i == 0:
        return nums[0]

    if i<0:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    pick = nums[i] + houseRobberMemoization(nums, dp, i-2)
    skip = houseRobberMemoization(nums, dp, i-1)

    dp[i] = max(pick, skip)
    return dp[i]

def houseRobberTabulation(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        pick = dp[i-2] + nums[i]
        skip = dp[i-1]

        dp[i] = max(pick, skip)

    return dp[n-1]

def houseRobberConstantSpace(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, n):
        pick = prev2 + nums[i]
        skip = prev1

        prev2 = prev1
        prev1 = max(pick, skip)

    return prev1

nums = list(map(int, input().split()))
print(houseRobber(nums))
