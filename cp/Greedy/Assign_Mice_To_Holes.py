'''
Given: mice -> mice positions, holes -> holes positions
Each mouse can move left/right
Each hole can hold only one mouse
Goal: Minimize the time so that all mice get into holes
Time = max dist any mouse travels
'''
# Ensure the slowest mice finishes as early as possible
def assign_mice_to_holes(mice, holes):
    # sort both arrays
    mice.sort()
    holes.sort()
    
    max_time = 0
    
    # pair corresponding elements
    for i in range(len(mice)):

        time = abs(mice[i]-holes[i])
        max_time = max(max_time, time)
    
    return max_time

mice = list(map(int, input().split()))
holes = list(map(int, input().split()))
print(assign_mice_to_holes(mice, holes))
