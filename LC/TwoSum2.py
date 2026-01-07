# 167. Two Sum II - Input Array Is Sorted
'''
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
''' 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            sum = nums[right] + nums[left]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left+=1
            else:
                right-=1
        return [-1, -1]
