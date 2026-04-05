'''
Given a grid: 1 -> land, 0 -> water
Find: Max area of any island
'''
def maxIsland(grid):
    n = len(grid); m = len(grid[0])
    maxArea = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                currArea = dfs(grid, i, j)
                maxArea = max(maxArea, currArea)
    
    return maxArea

def dfs(grid, i, j):
    n = len(grid); m = len(grid[0])
    
    # boundary + water check
    if i<0 or j<0 or i>=n or j>=m or grid[i][j] == 0:
        return 

    grid[i][j] = 0 # mark visited

    # count current + neighbors
    return (
        1
        + dfs(grid, i-1, j)
        + dfs(grid, i+1, j)
        + dfs(grid, i, j-1)
        + dfs(grid, i, j+1)
    )

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
