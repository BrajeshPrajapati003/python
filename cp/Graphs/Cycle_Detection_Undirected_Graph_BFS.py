'''
Detect cycle in an undirected graph using BFS
'''
from collections import deque

def hasCycleUndirectedBFS(n, graph):
    vis = [False]*n

    for i in range(n):
        if not vis[i]:

            q = deque()
            q.append(i, -1) # (node, parent)
            vis[i] = True

            while q:
                node, parent = q.popleft()

                for nei in graph[node]:

                    if not vis[nei]:
                        vis[nei] = True
                        q.append((nei, node))

                    elif nei!= parent:
                        return True # cycle found
    
    return False
