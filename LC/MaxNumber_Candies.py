# 1431 -> Kids With the Greatest Number of Candies

# def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         max = candies[0]
#         for i in candies:
#             if i > max:
#                 max = i

#         ans = []
#         for i in candies:
#             if i + extraCandies >= max :
#                 ans.append(bool(1)) # ans.append(bool(True))
#             else :
#                 ans.append(bool(0)) # ans.append(bool(False))
        
#         return ans

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [(i + extraCandies) >= max(candies) for i in candies]

