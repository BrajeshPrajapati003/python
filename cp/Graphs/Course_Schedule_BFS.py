'''
Given:
    courses = no. of courses
    prerequisites = [[a,b]];
    Meaning: b->a (you must complete b before a)
Goal: Can you finish all courses?
'''
from collections import deque

def canFinish(courses, prerequisites):

    graph = [[] for _ in range(courses)]
    indegree = [0]*courses

    # build graph
    for a, b in prerequisites:
        graph[b].append(a)   # b → a
        indegree[a] += 1

    q = deque()

    # add indegree 0 nodes
    for i in range(courses):
        if indegree[i] == 0:
            q.append(i)

    count = 0

    while q:
        node = q.popleft()
        count += 1

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return count == courses
