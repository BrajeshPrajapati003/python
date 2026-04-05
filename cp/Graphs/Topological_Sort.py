'''
You're Given tasks with dependencies: A->B->C
Meaning: A must be done before B, B before C
Goal: Find a valid order of tasks
'''
from collections import deque

def topoSort(graph, n):
    
    # calc indegree
    indegree = [0]*n

    for u in range(n):
        for v in graph[u]: # v -> nei or dest node
            indegree[v] += 1 # Edge: u->v
    
    # add nodes with indegree 0
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []

    # BFS (Kahn's)
    while q:
        node = q.popleft()
        topo.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1

            # if indegree becomes 0 -> ready to process
            if indegree[nei] == 0:
                q.append(nei)

    if len(topo) == n: # check cycle
        return topo
    else:
        return [] # cycle exists
