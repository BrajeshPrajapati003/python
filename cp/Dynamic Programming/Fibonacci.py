'''
Fibonacci Numbers: 0, 1, 1, 2, 3, 5
'''

def fibonacci(n):
    # return fibonacciRecursion(n)
    # dp = [-1]*(n+1)
    # dp[0] = 0; dp[1] = 1
    # return fibonacciMemoization(n, dp)
    # return fibonacciTabulation(n)
    return fibonacciConstantSpace(n)

def fibonacciRecursion(n):
    if(n<=1):
        return n
    
    return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

def fibonacciMemoization(n, dp):
    if n<=1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibonacciMemoization(n-1, dp) + fibonacciMemoization(n-2, dp)
    return dp[n]

def fibonacciTabulation(n):
    if n <= 1:
        return n
    
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]

def fibonacciConstantSpace(n):
    if n<=1:
        return n
    
    prev2, prev1 = 0, 1
    for i in range(2, n+1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr

    return prev1

n = int(input())
print(fibonacci(n))
