# 1137 -> N-th Tribonacci Number

# class Solution:
#     def tribonacci(self, n: int) -> int: #! TLE
#         if(n == 0 or n == 1):
#             return n
#         elif(n == 2):
#             return 1
#         else:
#             return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


class Solution:
    def tribonacci(self, n: int) -> int:
        set = {0:0, 1:1, 2:1}
        def f(x):
            if x in set:
                return set[x]
            else:
                set[x] = f(x-1) + f(x-2) + f(x-3)
                return set[x]
        return f(n)
    
