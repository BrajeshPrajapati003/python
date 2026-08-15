'''
724.
Given an integer array nums, find the pivot index.

The pivot index is the index where the sum of all elements strictly to the left is equal to the sum of all elements strictly to the right.

If the pivot is at index 0, the left sum is 0.
If the pivot is at the last index, the right sum is 0.
Return the leftmost pivot index.
If no pivot exists, return -1.
'''
def pivotIndex(nums):
    leftSum = 0
    total = 0
    for val in nums:
        total += val

    rightSum = 0
    for i in range(len(nums)):
        
        rightSum = total-leftSum-nums[i]
        if rightSum == leftSum:
            return i
        
        leftSum += nums[i]

    return -1

nums = list(map(int, input().split()))
print(pivotIndex(nums))
