# 1365 -> How Many Numbers Are Smaller Than the Current Number

# def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in nums:
#             count = 0
#             for j in nums:
#                 if j < i:
#                     count += 1
#             ans.append(count)
#         return ans

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    numSort = sorted(nums)
    count = {}
    currCount = 0
    for i in numSort:
         count.setdefault(i, currCount)
         currCount += 1
    return [count[i] for i in nums]

