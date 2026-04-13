'''
A prime number is a natural number greater than 1 and has exactly 2 divisors which are 1 and the number itself.

You are given a prime number n, find any 2 prime numbers a and b such that a+b=n or state that no such pair of primes exists.

Input
5

Output
2 3
'''
n = int(input())

def checkPrime(n):
    if n ==0 or n == 1:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        
        i += 1

if (checkPrime(n-2)):
    print(2, n-2)
else:
    print(-1)

