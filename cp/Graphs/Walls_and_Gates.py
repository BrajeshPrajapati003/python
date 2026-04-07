'''
Given a grid:
    0 -> gate (starting point), -1 -> wall (blocked), INF (2147483647) -> empty room (needs distance)
Task:
    Fill each empty room with distance to nearest gate
    If unreachable -> keep it
'''

# idea: instead of going from each room -> gate
# we go from all gates -> rooms
# as nearest gate will reach a room 1st  automatically (BFS property)

from collections import deque

def wallsAndGates(rooms):
    n, m = len(rooms), len(rooms[0])
    q = deque()

    INF = 2147483647

    # Add all gates to queue
    for i in range(n):
        for j in range(m):
            if rooms[i][j] == 0:
                q.append((i, j))

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check valid + unvisited room
            if 0 <= nx < n and 0 <= ny < m and rooms[nx][ny] == INF:

                # Update distance
                rooms[nx][ny] = rooms[x][y] + 1 # parent dist + 1

                # Push into queue
                q.append((nx, ny))
