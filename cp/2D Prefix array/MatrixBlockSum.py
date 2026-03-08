'''
Given: mat of size n*m and an integer k.
For every cell (i, j):
Return sum of all elements in square:
rows   from i-k to i+k
cols   from j-k to j+k
(Clamped inside matrix bounds)
'''

class MatrixBlockSum:
    def matrixBlockSum(self, mat, k):
        n, m = len(mat), len(mat[0])

        # Create (n+1) x (m+1) prefix matrix to simplify boundary handling
        pref = [[0] * (m+1) for _ in range(n+1)]

        # Build 2D prefix sum
        # pref[i][j] stores sum of rectangle (0,0) → (i-1,j-1)
        for i in range(1, n+1):
            for j in range(1, m+1):
                pref[i][j] = (
                    mat[i-1][j-1]    # current cell
                    + pref[i-1][j]   # top
                    + pref[i][j-1]   # left
                    - pref[i-1][j-1] # remove double-count
                )

        ans = [[0]*m for _ in range(n)]

        # Compute block sum for each cell
        for i in range(n):
            for j in range(m):
                # Clamp block boundaries within matrix limits
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(n-1, i+k)
                c2 = min(m-1, j+k)

                # Convert to 1-based indexing for prefix usage
                r1 += 1; c1 += 1
                r2 += 1; c2 += 1

                # Inclusion–exclusion to get submatrix sum in O(1)
                ans[i][j] = (
                    pref[r2][c2]
                    - pref[r1-1][c2]
                    - pref[r2][c1-1]
                    + pref[r1-1][c1-1]
                )

        return ans


n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

k = int(input())

obj = MatrixBlockSum()
res = obj.matrixBlockSum(mat, k)

for row in res:
    print(" ".join(map(str, row)))
