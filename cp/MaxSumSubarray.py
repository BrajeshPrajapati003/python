# max sum subarray of size k
def maxSumSubarray(nums: list, k: int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for r in range(k, len(nums)):
        window_sum += nums[r] - nums[r-k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum

nums = list(map(int, input().split()))
k = int(input())

print(maxSumSubarray(nums, k))
