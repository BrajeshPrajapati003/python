'''
2574. Left and Right sum difference
Given an integer array nums, create an array answer where:
    answer[i] = |leftSum[i] - rightSum[i]|
Where:
    leftSum[i] = sum of all elements strictly to the left of i
    rightSum[i] = sum of all elements strictly to the right of i
    |x| means absolute value.
'''

def leftRightSumDifference(nums):

    ans = []
    leftSum = rightSum = 0

    total = 0
    for val in nums:
        total += val

    for i in range(len(nums)):
        rightSum = total - leftSum - nums[i]

        x = leftSum - rightSum
        ans.append(abs(x))
        
        leftSum += nums[i]
    
    return ans

nums = list(map(int, input().split()))
print(leftRightSumDifference(nums))
