'''
Given a binary matrix (0 & 1): Count how many submatrices contain only 1s.
'''

import sys

def count_submatrices(mat):
    n, m = len(mat), len(mat[0])

    # heights[j] stores number of consecutive 1s ending at current row for column j
    heights = [0] * m

    total = 0  # total number of valid submatrices

    for i in range(n):

        # Update histogram heights for current row
        for j in range(m):
            if mat[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        # Monotonic stack to maintain increasing heights
        stack = []

        # count[j] = number of submatrices ending at column j in this row
        count = [0] * m

        sum_row = 0  # total submatrices using row i as bottom

        for j in range(m):

            # Maintain increasing stack (remove taller bars)
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()

            if stack:
                prev = stack[-1]  # index of previous smaller height

                # Extend rectangles from prev
                count[j] = count[prev] + heights[j] * (j - prev)
            else:
                # If no smaller height to the left
                count[j] = heights[j] * (j + 1)

            stack.append(j)

            # Add submatrices ending at column j
            sum_row += count[j]

        # Add all submatrices with bottom row = i
        total += sum_row

    return total


# Read matrix from input until EOF
mat = [list(map(int, line.split())) for line in sys.stdin]

print(count_submatrices(mat))
