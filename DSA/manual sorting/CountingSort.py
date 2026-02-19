
# Counting Sort (for +ve numbers only)
def counting_sort(nums: list[int]) -> list:
    if not nums:
        return nums
    
    max_val = max(nums)
    count = [0] * (max_val+1)

    # count freq
    for num in nums:
        count[num] += 1

    # Build sorted array
    sorted_nums = []
    for i in range(len(count)):
        sorted_nums.extend([i]*count[i])

    return sorted_nums



# Counting Sort (handles -ve numbers as well)
def counting_sort(nums):
    if not nums:
        return nums
    
    min_val = min(nums)
    max_val = max(nums)

    count = [0]*(max_val - min_val + 1)

    # count freq
    for num in nums:
        count[num - min_val] += 1
    
    # build sorted array
    sorted_nums = []
    for i in range(len(count)):
        sorted_nums.extend([i+min_val] * count[i])

    return sorted_nums
