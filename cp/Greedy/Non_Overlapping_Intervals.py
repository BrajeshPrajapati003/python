'''
Given: intervals = [[start, end],...]
You need to remove min no. of intervals so that the rest are non-overlapping
Return: min removals
'''
import sys

#! instead of removing bad ones, select max good ones
def eraseOverlappingIntervals(intervals): # intervals = [[start, end],...]
    intervals.sort(key=lambda x:x[1]) # sort by end time

    last_end = 0
    nonOverlapping = 0

    # count non-overlapping intervals
    for s, e in intervals:
        if last_end <= s:
            nonOverlapping+=1
            last_end = e
        
    # total - count
    return len(intervals)-nonOverlapping

intervals = [list(map(int, line.split())) for line in sys.stdin]
print(eraseOverlappingIntervals(intervals))
