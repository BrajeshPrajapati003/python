'''
Given:
    list of balloons: points[i] = [start, end]; each balloon is a horizontal interval
You can shoot an arrow at any x
An arrow bursts all balloons where start <= x <= end
Goal: Minimum no. of arrows to burst all balloons.
'''
import sys

def find_min_arrow_shots(points): # points = [[start, end],...]
    
    if not points:
        return 0
    
    # sort balloons by end coordinate
    points.sort(key=lambda x:x[1])

    # start with one arrow
    minArrows = 1

    # position of current arrow (end of first balloon)
    end = points[0][1]

    # traverse from 2nd balloon
    for s, e in points[1:]:
        
        # if current balloon doesn't overlap
        if s > end:
            minArrows += 1 # need new arrow
            end = e  # update arrow position

        # else: overlap -> do nothing (already burst)

    return minArrows

mat = [list(map(int, line.split())) for line in sys.stdin]
print(find_min_arrow_shots(mat))
