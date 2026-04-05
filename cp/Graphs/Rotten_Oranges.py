'''
Given a grid:
    0 = empty
    1 = fresh orange
    2 = rotten orange
Every minute, rotten oranges turn adjacent fresh oranges rotten.
Return the min time to rot all oranges
If impossible -> return -1
'''
from collections import deque

def orangesRotting(grid):
    n, m = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # add rotten + count fresh
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    
    time = 0
    dirs = [(1,0), (-1,0), (0, 1), (0, -1)]

    # BFS
    while q and fresh > 0:
        size = len(q)

        for _ in range(size): # one level = 1 min
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            
        time += 1

    # print("Minute:", time, "Queue:", list(q), "Fresh:", fresh)
    return time if fresh == 0 else -1

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(orangesRotting(grid))
