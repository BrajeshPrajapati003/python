# Bubble sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = list(map(int, input().split()))
sorted = bubble_sort(nums)

# print(", ".join(map(str, sorted))) # 1, 2, 3, 5, 5, 7, 8
print(" ".join(map(str, sorted))) # 1 2 3 5 5 7 8

