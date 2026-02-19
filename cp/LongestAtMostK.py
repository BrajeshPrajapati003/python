# longest subarray with sum <= k (non -ve numbers)
def longest_at_most_k(nums, k):
    l = maxLen = sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        while sum > k:
            sum -= nums[l]
            l += 1
        maxLen = max(r-l+1, maxLen)

    return maxLen

