'''
You are given a matrix. Answer Q queries.
Each query gives:
r1 c1 r2 c2
Return the sum of elements inside that rectangle (inclusive).
'''

class Prefix2D:
    def __init__(self, mat):
        n, m = len(mat), len(mat[0])

        # Extra row & column -> avoid boundary checks
        self.pref = [[0] * (m + 1) for _ in range(n + 1)]

        # Build 2D prefix sum
        # pref[i][j] stores sum of rectangle from (0,0) to (i-1,j-1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.pref[i][j] = (
                    mat[i - 1][j - 1]         # current cell
                    + self.pref[i - 1][j]     # top rectangle
                    + self.pref[i][j - 1]     # left rectangle
                    - self.pref[i - 1][j - 1] # remove double counted area
                )

    def query(self, r1, c1, r2, c2):
        # Convert to 1-based indexing for prefix matrix
        r1 += 1; c1 += 1
        r2 += 1; c2 += 1

        # Apply inclusion-exclusion principle
        return (
            self.pref[r2][c2]             # total up to bottom-right
            - self.pref[r1 - 1][c2]       # remove top excess
            - self.pref[r2][c1 - 1]       # remove left excess
            + self.pref[r1 - 1][c1 - 1]   # add back removed overlap
        )


n, m = map(int, input().split())

# Read matrix row by row
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

# Read query coordinates (0-based assumed)
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

prefix = Prefix2D(mat)
print(prefix.query(r1, c1, r2, c2))
