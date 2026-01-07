# 1 -> Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        n = len(nums)
        for i in range(n):
            rem = target-nums[i]
            if rem in dict1:
                return [dict1[rem], i]
            dict1[nums[i]] = i
