'''
Given a grid:
    0 -> src, 1 -> needs distance
For every cell, find: Distance to nearest 0

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
from collections import deque
def updateMatrix(mat):
    n = len(mat); m = len(mat[0])
    q = deque()

    # push all 0s, mark 1s as -1
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                q.append((i,j))
            elif mat[i][j] == 1:
                mat[i][j] = -1 # unvisited (-1)
    
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # BFS
    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = dx+x, dy+y

            if 0<=nx<n and 0<=ny<m and mat[nx][ny] == -1:
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx,ny))

    return mat
