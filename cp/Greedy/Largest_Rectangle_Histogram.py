'''
Given heights: [2, 1, 5, 6, 2, 3]
Each value = bar heights
width = 1
Find largest rectangle area
Output: 10
'''
def largest_rectangle(heights):
    n = len(heights)
    stack = [] # stores indices of bars (increasing heights)
    max_area = 0

    for i in range(n+1):
        
        # treat last iteration as height = 0
        # this forces all remaining bars to be processed
        curr = heights[i] if i<n else 0

        # if current bar is smaller, it means:
        # "we can't extend previous taller bars anymore"
        while stack and curr < heights[stack[-1]]:

            # take the bar which is now "finished"
            h = heights[stack.pop()]

            # now think:
            # this bar was the smallest in some range

            if not stack:
                # no smaller bar on the left
                # so it extends all the way to idx 0
                width = i
            else:
                # left boundary = stack[-1] (smaller bar)
                # right boundary = i (current smaller bar)

                # we exclude both boundaries
                # so valid width is only in between
                width = i - stack[-1] - 1
            
            # area formed with this height
            max_area = max(max_area, h * width)

        # push current idx
        # meaning: "this bar might extend further" [2,2,2,2]
        stack.append(i)
    
    return max_area

print(largest_rectangle([2, 1, 5, 6, 2, 3])) # 10
