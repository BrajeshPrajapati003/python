'''
Given grid:
    0 -> human
    1 -> zombie
Each minute: zombie infects adjacent humans
Return time to infect all humans
If impossible -> return -1
'''
from collections import deque

def zombieInfection(grid):
    n = len(grid); m = len(grid[0])
    q = deque()

    humans = 0

    # add all zombies & count humans
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                humans += 1
            else:
                q.append((i, j))
    
    time = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q and humans > 0:
        size = len(q)

        for _ in range(size): # 1 bfs level = 1 minute
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    humans -= 1
                    q.append((nx, ny))
        
        time += 1
    
    return time if humans == 0 else -1
