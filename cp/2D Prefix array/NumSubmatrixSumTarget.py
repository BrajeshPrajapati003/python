'''
Given: Matrix mat & Integer K
Return:
Number of submatrices whose sum equals K.
'''

from collections import defaultdict

class NumSubmatrixSumTarget:
    def numSubmatrixSumTarget(self, mat, target):
        n, m = len(mat), len(mat[0])
        count = 0

        # Fix top row
        for top in range(n):
            # Store compressed column sums
            colSum = [0]*m

            # Fix bottom row
            for bottom in range(top, n):
                # update column sums
                for c in range(m):
                    colSum[c] += mat[bottom][c]

                # now count subarrays in colsum with sum = target
                prefSum = 0
                freq = defaultdict(int)
                freq[0] = 1

                for val in colSum:
                    prefSum += val
                    count += freq[prefSum - target]
                    freq[prefSum] += 1

        return count

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

k = int(input())

obj = NumSubmatrixSumTarget()
res = obj.numSubmatrixSumTarget(mat, k)

print(res)
