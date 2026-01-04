# 509 -> Fibonacci Number

# class Solution:
#     def fib(self, n: int) -> int:
#         if(n == 0 or n == 1):
#             return n
#         else:
#             return self.fib(n-1) + self.fib(n-2) #! self -> object oriented code
        


class Solution:
    def fib(self, n: int) -> int:
        set = {0:0, 1:1}
        def f(x):
            if x in set:
                return set[x]
            else:
                set[x]=f(x-1)+f(x-2)
                return set[x]

        return f(n)
    
