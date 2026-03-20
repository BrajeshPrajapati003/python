'''
Given: tasks = ["A","A","A","B","B","B"], cooling time (n) = 2
Same tasks must be separated by at least n units
Each unit: either executes a task, or stay idle
Goal: Min. time to finish all tasks
'''
from collections import Counter

def leastInterval(tasks, n):
    freq = Counter(tasks)

    maxFreq = max(freq.values())

    # count how many tasks have max freq
    countMax = sum(1 for f in freq.values() if f == maxFreq)

    # apply formula:
    # blocks = maxFreq-1 
    # block size = n+1
    # + last group of max elements
    time = (maxFreq - 1) * (n + 1) + countMax

    # enough tasks -> len(tasks)
    # not enough tasks -> idle needed (A A A) -> take max(len(tasks), time)
    return max(len(tasks), time) 

tasks = list(map(str, input().split()))
n = int(input())

print(leastInterval(tasks, n))
