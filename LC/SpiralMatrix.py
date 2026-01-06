# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        total = n*m
        ans = []
        c = 0

        colStart = 0
        rowStart = 0
        colEnd = m-1
        rowEnd = n-1

        while c<total:
            #rowStart, colStart -> colEnd
            for i in range(colStart, colEnd+1):
                ans.append(matrix[rowStart][i])
                c+=1
            rowStart+=1

            if c==total:
                break
            
            #colEnd, rowStart -> rowEnd
            for i in range(rowStart, rowEnd+1):
                ans.append(matrix[i][colEnd])
                c+=1
            colEnd-=1

            if c==total:
                break
            
            #rowEnd, colEnd -> colStart
            for i in range(colEnd, colStart-1,-1):
                ans.append(matrix[rowEnd][i])
                c+=1
            rowEnd-=1

            if c==total:
                break
            

            #colStart, rowEnd -> rowStart
            for i in range(rowEnd, rowStart-1, -1):
                ans.append(matrix[i][colStart])
                c+=1
            colStart+=1

            if c==total:
                break
            
        return ans
