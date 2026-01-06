# 80 -> Remove Duplicates from Sorted Array II (same elements can occur at most twice)
# Return k after placing the final result in the first k slots of nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(2, len(nums)):
            if nums[k-1] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1
    
