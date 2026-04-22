'''
You've given a snake of length 2 on a grid.
Start: (0, 0) -> (0, 1) (horizontal)
Target:  (n-1, n-2) -> (n-1, n-1) 

Goal: Min. moves to reach target
Moves allowed:
    → move right
    ↓ move down
    ↻ rotate clockwise / anticlockwise
'''

# idea: node = (row, col, orientation)
# where:
    # (row, col) = tail position
    # orientation = 0 -> horizontal, 1 -> vertical

# same cell but diff. orientation = diff. state
# (2, 2, horizontal) != (2, 2, vertical) -> need state

# possible moves:
    # if horizontal: Snake (r,c) (r,c+1) -> 1. right, 2. down, 3. clockwise
    # if vertical: Snake (r,c) (r+1,c) -> 1. down, 2. right, 3. anti-clockwise

from collections import deque

def minimumMoves(grid):
    n = len(grid)

    # (row, col, orientation)
    # orientation: 0 = horizontal, 1 = vertical
    q = deque([(0, 0, 0, 0)]) # r, c, orient, steps
    vis = set([(0, 0, 0)])

    while q:
        r, c, orient, steps = q.popleft()

        # target reached
        if r == n-1 and c == n-2 and orient == 0:
            return steps

        if orient == 0: # horizontal

            # move right
            if c+2 < n and grid[r][c+2] == 0:
                if (r, c+1, 0) not in vis:
                    vis.add((r, c+1, 0))
                    q.append((r, c+1, 0, steps+1))

            # move down
            if r+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
                if (r+1, c, 0) not in vis:
                    vis.add((r+1, c, 0))
                    q.append((r+1, c, 0, steps+1))

                # rotate clockwise
                if (r, c, 1) not in vis:
                    vis.add((r, c, 1))
                    q.append((r, c, 1, steps+1))
        
        else: # vertical

            # move down
            if r+2 < n and grid[r+2][c] == 0:
                if (r+1, c, 1) not in vis:
                    vis.add((r+1, c, 1))
                    q.append((r+1, c, 1, steps+1))

            # move right
            if c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
                if (r, c+1, 1) not in vis:
                    vis.add((r, c+1, 1))
                    q.append((r, c+1, 1, steps+1))

                # rotate anti-clockwise
                if (r, c, 0) not in vis:
                    vis.add((r, c, 0))
                    q.append((r, c, 0, steps+1))
    
    return -1
