'''
Given:
    courses = no. of courses
    prerequisites = [[a,b]];
    Meaning: b->a (you must complete b before a)
Goal: Can you finish all courses?
'''
# course schedule using DFS (vis and path array)
from typing import List

def canFinish(self, courses: int, prerequisites: List[List[int]]) -> bool:
        
    graph = [[] for _ in range(courses)]

    for a, b in prerequisites:
        graph[b].append(a) # b -> a
    
    vis = [False]*courses
    path = [False]*courses

    def dfs(node):
        vis[node] = True
        path[node] = True

        for nei in graph[node]:
            if not vis[nei]:
                if dfs(nei):
                    return True
            elif path[nei]:
                return True

        path[node] = False
        return False
    
    for i in range(courses):
        if not vis[i]:
            if dfs(i): # cycle detected
                return False

    return True
