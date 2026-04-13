'''
Given a grid: 1 -> land, 0 -> water
Find: The water cell that is FARTHEST from any land
Return that distance.
If all land or all water -> return -1
'''
from collections import deque
from typing import List

def maxDistance(grid: List[List[int]]) -> int:
    n = len(grid); m = len(grid[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1: # push all land
                q.append((i, j))

    # edge case (no land -> -1, no water -> -1)
    if not q or len(q) == n*n:
        return -1

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # dist = -1, because BFS increments after processing a level
    # so starting at -1 aligns the first processed level (land) with distance 0.
    dist = -1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = dx+x, dy+y

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                    grid[nx][ny] = 1 # mark visited
                    q.append((nx, ny))
        dist += 1  
    return dist          
