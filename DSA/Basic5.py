
# Bubble Sort
class BubbleSortOptimized:
    def sortArray(self, nums: List[int]) -> List[int]:
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
    def sortArray(self, nums: List[int]) -> List[int]:
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
    def sortArray(nums : List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIdx = i
            for j in range(i+1, n):
                if nums[minIdx] > nums[j]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums
    


