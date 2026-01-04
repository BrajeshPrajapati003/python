# 1523 -> Count Odd Numbers in an Interval Range

# def countOdds(self, low: int, high: int) -> int: #! TLE
#         count = 0
#         # for i in range(low, high+1):
#         #     if i%2 != 0:
#         #         count += 1
#         # return count
#         if low%2 == 0:
#             for i in range(low+1, high+1, 2):
#                 count+=1
#         else:
#             for i in range(low, high+1, 2):
#                 count+=1
#         return count


def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - (low//2)

