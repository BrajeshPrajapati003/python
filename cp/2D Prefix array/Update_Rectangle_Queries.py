'''
Problem:
Start with an n*m matrix filled with 0.

Operations:
1. Update: add value 'val' to all cells inside rectangle
   (r1, c1) -> (r2, c2)

2. Query: return the sum of elements inside rectangle
   (r1, c1) -> (r2, c2)

Technique used:
- 2D Difference Matrix for fast updates
- 2D Prefix Sum for fast queries
'''

class MatrixHandler:
    def __init__(self, n, m):
        self.n = n
        self.m = m

        # Difference matrix (extra row/column avoids boundary checks)
        self.diff = [[0]*(m+1) for _ in range(n+1)]

    # Apply rectangle update
    def update(self, r1, c1, r2, c2, val):
        '''
        Difference matrix trick:
        +val at start
        -val after rectangle boundaries
        '''
        self.diff[r1][c1] += val
        self.diff[r1][c2+1] -= val
        self.diff[r2+1][c1] -= val
        self.diff[r2+1][c2+1] += val

    # Build final matrix and prefix sums
    def build(self):

        # Convert difference matrix → actual matrix
        for i in range(self.n):
            for j in range(self.m):

                if i > 0:
                    self.diff[i][j] += self.diff[i-1][j]

                if j > 0:
                    self.diff[i][j] += self.diff[i][j-1]

                if i > 0 and j > 0:
                    self.diff[i][j] -= self.diff[i-1][j-1]

        # Extract actual matrix (remove extra row/column)
        self.mat = [row[:self.m] for row in self.diff[:self.n]]

        # Build prefix sum matrix for queries
        self.pref = [[0]*(self.m+1) for _ in range(self.n+1)]

        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                self.pref[i][j] = (
                    self.mat[i-1][j-1]
                    + self.pref[i-1][j]
                    + self.pref[i][j-1]
                    - self.pref[i-1][j-1]
                )

    # Rectangle sum query
    def query(self, r1, c1, r2, c2):

        # Convert to 1-based indexing for prefix matrix
        r1 += 1; c1 += 1
        r2 += 1; c2 += 1

        return (
            self.pref[r2][c2]
            - self.pref[r1-1][c2]
            - self.pref[r2][c1-1]
            + self.pref[r1-1][c1-1]
        )
