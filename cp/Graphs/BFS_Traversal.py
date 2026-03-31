'''
BFS traversal in a graph
'''
from collections import deque

def bfs(graph, start):
    vis = set() # visited nodes
    q = deque([start]) # queue for BFS

    vis.add(start) # mark visited

    while q:
        front = q.popleft()
        print(front, end=" ")

        # visit all neighbors
        for nei in graph[front]:
            
            if nei not in vis:
                vis.add(nei)
                q.append(nei)

n = int(input()) # nodes

graph = [[] for _ in range(n+1)] # initialize adjacency list

e = int(input()) # edges

# take edges input
for _ in range(e):
    u, v = map(int, input().split())

    graph[u].append(v) # edge u -> v
    graph[v].append(u) # edge v -> u (undirected)


start = int(input()) # starting node

bfs(graph, start)
