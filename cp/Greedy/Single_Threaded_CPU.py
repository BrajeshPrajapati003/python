'''
Given: tasks[i] = [enqueueTime, processingTime]
CPU can process one task at a time
Rules:
    1. At time t, you can pick any task with enqueueTime <= t
    2. Choose task with:
        smallest processing time
        if tie -> smaller idx
    3. If no task available -> jump time forward
Return order of execution
Ex: tasks = [[1,2], [2,4], [3,2], [4,1]]
output: [0,2,3,1]
'''
import heapq

def getOrder(tasks):
    n = len(tasks)

    # add idx
    tasks = [(e,p,i) for i, (e,p) in enumerate(tasks)]

    # sort by enqueue time
    heap = []
    time = 0
    i = 0
    res = []

    while i<n or heap:

        # if no task available -> jump time
        if not heap and time < tasks[i][0]:
            time = tasks[i][0]
        
        # add all available tasks
        while i<n and tasks[i][0] <= time:
            e, p, idx = tasks[i]
            heapq.heappush(heap, (p, idx))
            i += 1

        # pick shortest task
        p, idx = heapq.heappop(heap)
        time += p
        res.append(idx)
    
    return res

tasks = [[1, 2], [2,4], [3,2], [4,1]]
print(getOrder(tasks)) # [0, 2, 3, 1]

