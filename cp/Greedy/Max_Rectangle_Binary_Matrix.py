'''
Given a binary matrix
Find largest rectangle of 1's
'''
def largest_rectangle(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n+1):
        curr = heights[i] if i<n else 0

        while stack and curr < heights[stack[-1]]:
            h = heights[stack.pop()]

            if not stack:
                width = i
            else:
                width = i-stack[-1]-1

            max_area = max(max_area, h*width)

        stack.append(i)

    return max_area

def max_rectangle(matrix):
    if not matrix:
        return 0
    
    cols = len(matrix[0])
    heights = [0]*cols
    max_area = 0

    for row in matrix:

        # build histogram
        for i in range(cols):
            if row[i] == 1:
                heights[i] += 1
            else:
                heights[i] = 0
        
        # solve histogram
        max_area = max(max_area, largest_rectangle(heights))

    return max_area

matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

print(max_rectangle(matrix)) # 6
