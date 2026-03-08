'''
Given matrix & integer k.
Return: The side length of the largest square submatrix whose sum <= k.
'''
def largest_square_sum_K(mat, k):
    n, m = len(mat), len(mat[0])

    # Build 2D prefix mat
    pref = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            pref[i][j] = (
                mat[i-1][j-1] 
                + pref[i-1][j] 
                + pref[i][j-1] 
                - pref[i-1][j-1]
            )

    maxSide = 0

    # Try every top-left corner
    # can be optimized using binary search on answer
    for i in range(n):
        for j in range(m):
            
            # Try increasing square sizes
            size = 1
            while i+size <= n and j+size <= m:
                
                r1, c1 = i, j
                r2, c2 = i+size-1, j+size-1

                # convert to 1-based
                r1 += 1; r2 += 1; c1 += 1; c2 += 1
                
                maxSide = (
                    pref[r2][c2]
                    - pref[r1-1][c2]
                    - pref[r2][c1-1]
                    + pref[r1-1][c1-1]
                )

                if maxSide <= k:
                    maxSide = max(maxSide, size)
                else:
                    # no need to increase further
                    break

                size += 1
    
    return maxSide

n = int(input())
m = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

k = int(input())
print(largest_square_sum_K(mat, k))
