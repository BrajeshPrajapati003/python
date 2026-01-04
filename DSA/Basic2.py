# i = 1
# while(i <= 5):
#     print(i)
#     i+=1

# ctx: print n numbers using recursion
# def printN(n):
#     if(n > 10):
#         return
#     else:
#         print(n)
#         printN(n+1)

# printN(1)

# ctx: print factorial using recursion
# def factorial(n) -> int:
#     if(n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# ctx: print nth fibonacci number
# def fibonacci(n) -> int:
#     if(n == 0 or n == 1) :
#         return n
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(6))

#! fibonacci Number

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
    
#! Tribonacci Number

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
    

#! GCD / HCF of two numbers

def gcd(a: int, b: int) -> int: # Euclidean Algorithm
    if(b == 0):
        return a
    return gcd(b, a%b)

#! LCM of two numbers

def lcm(a: int, b: int) -> int:
    return int(a*b/gcd(a,b))

print(gcd(20,4))
print(lcm(20,4))

