'''
Given a grid: 
    0 -> free cell, 1 -> blocked cell
    start -> (0, 0), end -> (n-1, n-1)
Goal: Find shortest path from start -> end
You can move in 8 directions: up, down, left, right, diagonals
'''
from collections import deque
from typing import List

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    n = len(grid)

    # edge case - check start cell
    if grid[0][0] == 1:
        return -1

    q = deque()
    q.append((0, 0, 1)) # (row, col, dist)

    # mark visited
    grid[0][0] = 1

    dirs = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    while q: # bfs from (0,0)
        x, y, dist = q.popleft() # track dist

        # reached destination
        if x == n-1 and y == n-1:
            return dist
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                q.append((nx, ny, dist + 1))
                grid[nx][ny] = 1 # mark visited
    
    return -1
