'''
LC 740. Delete and Earn
You are given an integer array nums.
You can perform the following operation any number of times:
    1. Choose an element nums[i] and earn its value in points.
    2. Delete every occurrence of nums[i] - 1 and nums[i] + 1 from the array.
    3. You can no longer earn points from the deleted elements.
Return the maximum points you can earn.
'''

def deleteAndEarn(nums) -> int:
    # points[x] = total points earned by taking every occurrence of x
    # Using Count Sort
    points = [0]*(max(nums)+1)
    for num in nums:
        points[num] += num

    # return deleteEarnRecursion(points, len(points)-1)

    # dp = [-1]*len(points)
    # return deleteEarnMemo(points, dp, len(points)-1)
    # return deleteEarnTabulation(points)
    return deleteEarnConstantSpace(points)

def deleteEarnRecursion(points, idx):
    if idx < 0:
        return 0

    take = points[idx] + deleteEarnRecursion(points, idx-2)
    skip = deleteEarnRecursion(points, idx-1)

    return max(take, skip)

def deleteEarnMemo(points, dp, idx):
    if idx < 0:
        return 0
    
    if dp[idx] != -1:
        return dp[idx]
    
    take = points[idx] + deleteEarnMemo(points, dp, idx-2)
    skip = deleteEarnMemo(points, dp, idx-1)

    dp[idx] = max(take, skip)
    return dp[idx]

def deleteEarnTabulation(points):
    n = len(points)

    if n == 1:
        return points[0]

    dp = [0]*n

    dp[0] = points[0]
    dp[1] = max(points[0], points[1])
    for i in range(2, n):
        take = points[i] + dp[i-2]
        skip = dp[i-1]

        dp[i] = max(take, skip)

    return dp[n-1]

def deleteEarnConstantSpace(points):
    n = len(points)

    if n == 1:
        return points[0]
        
    prev2 = points[0]
    prev1 = max(points[0], points[1])

    for i in range(2, n):
        take = prev2 + points[i]
        skip = prev1

        prev2 = prev1
        prev1 = max(take, skip)
    
    return prev1

nums = list(map(int, input().split()))
print(deleteAndEarn(nums))
