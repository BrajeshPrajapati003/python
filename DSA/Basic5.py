
# Bubble Sort
class BubbleSortOptimized:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            isSwap = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    isSwap = True
            if not isSwap:
                break
        return nums
    


# Insertion Sort
class InsertionSort:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            key = nums[i]
            j = i-1
            while j>=0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums



# Selection Sort
class SelectionSort:
    def sortArray(nums : list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            minIdx = i
            for j in range(i+1, n):
                if nums[minIdx] > nums[j]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums
    


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



