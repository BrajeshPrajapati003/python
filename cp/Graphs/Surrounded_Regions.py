'''
Given a grid:
    'X' -> blocked
    'O' -> open region
Task: convert all 'O' that are completely surrounded by 'X' into 'X'
'''
from typing import List

def surrounded_regions(board: List[List[int]]) -> None:
    n, m = len(board), len(board[0])

    # mark boundary connected '0' as safe ('S')
    for i in range(n):
        for j in range(m):
            if (i==0 or j==0 or i==n-1 or j==m-1) and board[i][j]=='O':
                dfs_mark(board, i, j)
    
    # convert remaining 'O' -> 'X'
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = 'X'

    # restore safe 'S' -> 'O'
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'S':
                board[i][j] = 'O'


def dfs_mark(board, i, j):
    n = len(board), len(board[0])

    if i<0 or j<0 or i>=n or j>=0 or board[i][j] != 'O':
        return
    
    board[i][j] = 'S' # mark safe

    dfs_mark(board, i-1, j); dfs_mark(board, i+1, j)
    dfs_mark(board, i, j-1), dfs_mark(board, i, j+1)

