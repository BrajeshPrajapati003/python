'''
Given: n nodes, edges list, src and dest
Return True if path exists from src -> dest
'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:

        # build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = [False]*n

        # return self.dfs(graph, src, dest, vis)
        return self.bfs(graph, src, dest, n)
    
    # using DFS
    def dfs(self, graph, node, dest, vis):

        if node == dest:
            return True
        
        vis[node] = True

        for nei in graph[node]:
            if not vis[nei]:
                if self.dfs(graph, nei, dest, vis):
                    return True
                
        return False

    # using BFS
    def bfs(self, graph, src, dest, n):
        vis = [False]*n

        q = deque([src])
        vis[src] = True

        while q:
            node = q.popleft()

            if node == dest:
                return True
            
            for nei in graph[node]:
                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)
            
        return False
