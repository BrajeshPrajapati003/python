'''
We're giving away nice huge bags containing number tiles! A bag we want to present to you contains n tiles. Each of them has a single number written on it — either 1 or 2.

However, there is one condition you must fulfill in order to receive the prize. You will need to put all the tiles from the bag in a sequence, in any order you wish. We will then compute the sums of all prefixes in the sequence, and then count how many of these sums are prime numbers. If you want to keep the prize, you will need to maximize the number of primes you get.

Input:
5
1 2 1 2 1

Output:
1 1 1 2 2
'''
import sys
input = sys.stdin.readline

n = int(input()) # 1st line
arr = list(map(int, input().split())) # 2nd line

twos = ones = 0 # twos = arr.count(2); ones = arr.count(1)
for val in arr:
    if val == 1:
        ones += 1
    else:
        twos += 1

if twos == 0:
    for _ in range(n):
        print(1, end=" ")
elif ones == 0:
    for _ in range(n):
        print(2, end=" ")
else:
    print(2, 1, end=" ")
    twos -= 1; ones -= 1

    for _ in range(twos):
        print(2, end=" ")

    for _ in range(ones):
        print(1, end=" ")
    
