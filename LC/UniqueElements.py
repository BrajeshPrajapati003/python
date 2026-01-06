# 26 -> Remove Duplicates from Sorted Array
# Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1
    
