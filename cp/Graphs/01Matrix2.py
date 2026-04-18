'''
Given a grid:
    0 -> src, 1 -> needs distance
For every cell, find: Distance to nearest 0

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
from collections import deque

def updateMatrix(mat):
    n, m = len(mat), len(mat[0])

    q = deque()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                mat[i][j] = float('inf') # meaning: not yet reached by any 0
            else:
                q.append((i, j))
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS + shortest path relaxation (like a mini Dijkstra without priority queue)
    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x+dx, y+dy

            # found a shorter path -> update
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] > mat[x][y] + 1:
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx, ny))
    
    return mat

# INF = "distance not yet optimized"
# CTX: Inf allows us to use relaxation logic and makes it closer to shortest path formulation
# ! This becomes Dijkstra when weights are added
