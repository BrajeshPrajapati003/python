'''
Given a 2D grid:
    grid[i][j] = '1' -> land
    grid[i][j] = '0' -> water
Goal: Count how many islands exist
'''

def numIslands(grid):
    n = len(grid); m = len(grid[0])
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

def dfs(grid, i, j):
    n = len(grid); m = len(grid[0])

    # boundary check + water check
    if i<0 or j<0 or i>=n or j>=m or grid[i][j] == '0':
        return

    # mark as visited
    grid[i][j] = '0'

    # explore all 4 directions
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)

n = int(input())
grid = [list(map(str, input().split())) for _ in range(n)]
print(numIslands(grid))
