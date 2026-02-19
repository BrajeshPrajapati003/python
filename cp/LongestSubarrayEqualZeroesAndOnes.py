# in binary array, length of the longest subarray with equal no. of 0's and 1's
def longestSubarrayLength(nums: list) -> int:
    map = {0:-1}
    maxLen = sum = 0
    
    for i in range(len(nums)):
        sum += 1 if nums[i] == 1 else -1
        
        if sum in map:
            maxLen = max(maxLen, i-map[sum])
        else:
            map[sum] = i

    return maxLen

