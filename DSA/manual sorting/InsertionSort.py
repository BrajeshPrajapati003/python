# Insertion Sort
def insertion_sort(nums):
    n = len(nums)
    for i in range(n):
        j = i-1
        key = nums[i]
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums = list(map(int, input().split()))
sorted = insertion_sort(nums)
print(" ".join(map(str, sorted)))
