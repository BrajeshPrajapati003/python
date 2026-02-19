# Bubble Sort (Optimized)
def bubble_sort_optimized(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swapped = True
        if not swapped:
            break
    return nums

nums = list(map(int, input().split()))
sorted = bubble_sort_optimized(nums)
print(" ".join(map(str, sorted)))
