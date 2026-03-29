'''
Given: intervals = [[start, end],...]
Each meeting needs a room
Meetings overlap -> need more rooms
Goal: Min number of rooms required
'''
# track earliest ending meeting
# Idea:
    # sort by start time
    # use min heap of end times
    # if earliest end <= curr start -> reuse room

import heapq

def min_rooms_heap(intervals):
    intervals.sort()

    # heap = active intervals tracker, heap size = concurrency
    heap = [] # store end times of ongoing meetings

    for s, e in intervals:

        # free room if possible
        if heap and heap[0] <= s:
            heapq.heappop(heap) # meeting ended -> room freed

        heapq.heappush(heap, e)

    return len(heap)

print(min_rooms_heap([[0,30],[5,10],[15,20]])) # 2
