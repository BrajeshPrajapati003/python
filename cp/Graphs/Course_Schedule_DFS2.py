'''
Given:
    courses = no. of courses
    prerequisites = [[a,b]];
    Meaning: b->a (you must complete b before a)
Goal: Can you finish all courses?
'''
# course schedule using DFS (only vis array)
from typing import List
def canFinish(self, courses: int, prerequisites: List[List[int]]) -> bool:
    
    graph = [[] for _ in range(courses)]

    # build graph
    for a, b in prerequisites:
        graph[b].append(a) # b -> a
    
    # 0 = unvisited, 1 = visiting (in curr path), 2 = visited (fully processed now backtrack)
    vis = [0]*courses

    def dfs(node):
        if vis[node] == 1: # cycle detected
            return False
        
        # already processed -> safe
        if vis[node] == 2:
            return True
        
        # mark curr node in path
        vis[node] = 1

        for nei in graph[node]:
            if not dfs(nei): # cycle found deeper
                return False
        
        # done exploring -> remove from path
        vis[node] = 2 # mark as done
        return True

    for i in range(courses):
        if not dfs(i):
            return False
    
    return True
