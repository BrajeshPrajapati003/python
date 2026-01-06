# 885. Spiral Matrix III
'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.
'''

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        n = rows*cols

        res = [[0,0] for _ in range(n)]
        res[0][0] = rStart
        res[0][1] = cStart

        count = 1
        step = 1
        index = 0

        while(count < n):
            for _ in range(2):
                dr, dc = directions[index%4]
                for _ in range(step):
                    rStart += dr
                    cStart += dc

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res[count][0] = rStart
                        res[count][1] = cStart
                        count += 1
                    
                index += 1
            step += 1

        return res
