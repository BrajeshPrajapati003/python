'''
Given a grid: 0 -> land & 1 -> water
Find: No. of islands completely surrounded by water
'''
from typing import List

def closedIsland(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    # remove boundary connected islands
    for i in range(n):
        for j in range(m):
            if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j] == 0:
                dfs(grid, i, j)
    
    # count remaining islands
    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                dfs(grid, i, j)
                islands += 1
    
    return islands

def dfs(grid, i, j):
    n, m = len(grid), len(grid[0])

    if i<0 or j<0 or i>=n or j>=m or grid[i][j] == 1:
        return
    
    grid[i][j] = 1 # land -> water

    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)
