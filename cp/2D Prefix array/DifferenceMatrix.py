'''
Your are given:
matrix of size n*m (initially 0)
Q operations - add x to rect from (r1, c1) to (r2, c2)
After all operations, print final matrix
'''
# 2D difference array
def apply_updates(n, m, queries):
    # Extra row/col -> boundary updates safely
    diff = [[0]*(m+1) for _ in range(n+1)]

    for r1, c1, r2, c2, val in queries:
        # start of rect
        diff[r1][c1] += val
        # stop after right
        if c2+1 < m:
            diff[r1][c2+1] -= val
        # stop after bottom
        if r2+1 < n:
            diff[r2+1][c1] -= val
        # restore overlap
        if r2+1 < n and c2+1 < m:
            diff[r2+1][c2+1] += val
        
    # ! we have created the diff mat with size n+1, m+1 so that boundary checks are done safely -> hence we don't need to check c2+1 < m and r2+1 < n conditions separately.
    # ! Here we've done to handle invalid inputs although not necessary.

    # Build final matrix using prefix sums
    for i in range(n):
        for j in range(m):
            # accumulate from top
            if i>0:
                diff[i][j] += diff[i-1][j]
            # accumulate from left
            if j>0:
                diff[i][j] += diff[i][j-1]
            # remove double counted area
            if i>0 and j>0: 
                diff[i][j] -= diff[i-1][j-1]
    
    # Extract n*m matrix
    res = [row[:m] for row in diff[:n]]
    return res

n = int(input())
m = int(input())
q = int(input()) # no. of queries
queries = [list(map(int, input().split())) for _ in range(q)]

res = apply_updates(n, m, queries)
for row in res:
    print(*row)
