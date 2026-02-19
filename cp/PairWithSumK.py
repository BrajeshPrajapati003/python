# length of the longest pair having sum = k (sorted array)
def pair_with_sum_k(nums, k):
    l = 0
    r = len(nums)-1
    while l < r:
        sum = nums[l] + nums[r]
        if sum == k:
            return True
        elif sum < k:
            l += 1
        else:
            r -= 1
    return False
        
