class Prefix2D:
    def __init__(self, mat):
        n, m = len(mat), len(mat[0])
        self.pref = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                self.pref[i][j] = (
                    mat[i-1][j-1]
                    + self.pref[i-1][j]
                    + self.pref[i][j-1]
                    - self.pref[i-1][j-1]
                )
    
    def query(self, r1, c1, r2, c2):
        r1 += 1; c1 += 1; r2 += 1; c2 += 1
        return (
            self.pref[r2][c2]
            - self.pref[r1-1][c2]
            - self.pref[r2][c1-1]
            + self.pref[r1-1][c1-1]
        )
    

n, m = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

prefix = Prefix2D(mat)
print(prefix.query(r1, c1, r2, c2))

