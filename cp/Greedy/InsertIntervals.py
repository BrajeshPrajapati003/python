'''
Insert multiple new intervals into existing intervals.
'''
def insert_multiple_intervals(intervals, newIntervals):

    # add all new intervals to existing intervals
    intervals.extend(newIntervals)

    # sort everything by start
    intervals.sort(key=lambda x:x[0])

    # merge like normal
    res = []
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    
    return res

intervals = [[1,3], [6,9]]
newIntervals = [[2,5], [10,12]]
print(insert_multiple_intervals(intervals, newIntervals)) # [[1, 5], [6, 9], [10, 12]]
