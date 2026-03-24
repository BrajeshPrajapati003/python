'''
Given:
    a list of non-overlapping, sorted intervals
    a new interval
Insert it into the list
Merge if needed
Return final intervals

Testcase:
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
Output: [[1, 5], [6, 9]]
'''
def insertInterval(intervals, newInterval):
    n = len(intervals)
    i = 0
    res = []

    # 1. before overlap
    # add all intervals before newInterval
    while i<n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i+=1

    # 2. merge overlaps
    # merge overlapping intervals
    while i<n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i+=1
    
    res.append(newInterval)

    # 3. remaining
    # add remaining intervals
    while i<n:
        res.append(intervals[i])
        i+=1
    
    return res

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(insertInterval(intervals, newInterval)) # [[1, 5], [6,9]]
