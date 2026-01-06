# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

class Solution:
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    #     ans = []
    #     for i in nums:
    #         if i&1 == 0:
    #             ans.append(i)
            
    #     for i in nums:
    #         if i&1 != 0:
    #             ans.append(i)
    #     return ans
    

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        for i in nums:
            if nums[i]&1 == 0:
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp
                start += 1
        return nums

