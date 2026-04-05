'''
Detect cycle in a directed using BFS (Kahn's algo)
'''
from collections import deque

def hasCycleDirectedBFS(n, graph):
    indegree = [0]*n

    # calc indegree
    for i in range(n):
        for nei in graph[i]:
            indegree[nei] += 1
    
    q = deque()

    # push nodes with indegree 0
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    count = 0

    # if we can't process all nodes -> cycle exists
    # because nodes in cycle will never reach indegree 0
    while q:
        node = q.popleft()
        count += 1

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    return count != n # True = cycle exists
