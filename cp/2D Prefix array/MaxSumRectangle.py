'''
Maximum sum rectangle (submatrix) in a matrix.
Return the maximum sum
'''
def maxSumRectangle(mat):
    n, m = len(mat), len(mat[0])
    maxSum = float('-inf')

    # fix top row
    for top in range(n):
        # compressed columns
        colSum = [0]*m
        
        # fix bottom row
        for bottom in range(top, n):
            
            # update colSum
            for c in range(m):
                colSum[c] += mat[bottom][c]

            # apply Kadane's algo
            currSum = colSum[0]
            for i in range(1, m):
                currSum = max(currSum+colSum[i], colSum[i])
                maxSum = max(currSum, maxSum)
    
    return maxSum

n = int(input())
m = int(input())
mat = []
for row in range(n):
    mat.append(list(map(int, input().split())))

print(maxSumRectangle(mat))

