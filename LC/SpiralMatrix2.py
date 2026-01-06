# 59. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        val = 1
        ans = [[0]*n for _ in range(n)]

        # rowStart = 0
        # colStart = 0
        # colEnd = n-1
        # rowEnd = n-1
        rowStart, rowEnd = 0, n-1
        colStart, colEnd = 0, n-1

        while(rowStart <= rowEnd and colStart <= colEnd):

            # rowStart, colStart -> colEnd
            for i in range(colStart, colEnd+1):
                ans[rowStart][i] = val
                val+=1
            rowStart+=1

            # colEnd, rowStart -> rowEnd
            for i in range(rowStart, rowEnd+1):
                ans[i][colEnd] = val
                val+=1
            colEnd-=1

            # rowEnd, colEnd -> colStart
            for i in range(colEnd, colStart-1, -1):
                ans[rowEnd][i] = val
                val+=1
            rowEnd-=1

            # colStart, rowEnd - rowStart   
            for i in range(rowEnd, rowStart-1, -1):
                ans[i][colStart] = val
                val+=1
            colStart+=1
        
        return ans
