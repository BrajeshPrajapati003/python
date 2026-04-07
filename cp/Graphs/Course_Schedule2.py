'''
Same as course schedule 1 but:
Goal: Return a valid order of courses
    If impossible (cycle) -> return []
'''
from typing import List
from collections import deque
def findOrder(courses: int, prerequisites: List[List[int]]) -> List[int]:
    
    graph = [[] for _ in range(courses)]
    indegree = [0]*courses

    # build graph
    for a, b in prerequisites:
        graph[b].append(a) # b->a
        indegree[a] += 1
        
    q = deque()
    for i in range(courses):
        if indegree[i] == 0:
            q.append(i)        
    
    order = []
    while q:
        node = q.popleft()
        order.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return order if len(order) == courses else []
