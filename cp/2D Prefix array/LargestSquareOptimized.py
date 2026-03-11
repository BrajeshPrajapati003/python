'''
Largest square sum <= k using binary search on answer
'''

def largest_square_binary(mat, k):
    n,m = len(mat), len(mat[0])

    # build prefix sum matrix
    pref = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            pref[i][j] = (
                mat[i-1][j-1] 
                + pref[i-1][j] 
                + pref[i][j-1] 
                - pref[i-1][j-1]
            )

    # function to check if square of given size exists
    def exists(size):
        for i in range(n-size+1):
            for j in range(m-size+1):
                r1, c1 = i+1, j+1
                r2, c2 = i+size, j+size

                square_sum = (
                    pref[r2][c2]
                    - pref[r1-1][c2]
                    - pref[r2][c1-1]
                    + pref[r1-1][c1-1]
                )

                if square_sum <= k:
                    return True
        return False
    
    # binary search on side length
    low = 0
    high = min(n, m)
    ans = 0
    while low <= high:
        mid = (low+high)//2
        if exists(mid):
            ans = mid
            low = mid+1 # try larger
        else:
            high = mid-1 # try smaller
        
    return ans


n = int(input())
m = int(input())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

k = int(input())

print(largest_square_binary(mat, k))
