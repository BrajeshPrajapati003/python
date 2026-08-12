

''' Best time to buy and sell stock
'''
def stock(nums) -> int:

    leftMin = float("inf")
    maxProfit = 0
    for i in range(len(nums)):
        
        if leftMin > nums[i]:
            leftMin = nums[i]
        
        maxProfit = max(maxProfit, nums[i]-leftMin)

    return maxProfit

# print(stock(list(map(int, input().split(",")))))

''' Max subarray sum
'''
def kadane(nums):
    currSum, maxSum = 0,0
    for i in range(len(nums)):
        if currSum < 0:
            currSum = nums[i]
        else:
            currSum += nums[i]
        
        maxSum = max(maxSum, currSum)
    
    return maxSum

# print(kadane(list(map(int, input().split(",")))))

'''Move zeroes to last
'''
def moveZeroes(nums):

    i = j = 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    
    return nums

# print(moveZeroes(list(map(int, input().split(",")))))

'''Merge intervals
'''
def mergeIntervals(intervals):

    intervals.sort()
    last_end = intervals[0][1]
    new_intervals = []
    curr_interval = []
    for s, e in intervals:

        if last_end >= s:
            new_interval[0] = s
            new_intervals[k][1] = e