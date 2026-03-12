'''
You're given basket positions pos[].
Place m balls such that the minimum distance between any two balls is maximized.
'''
def max_magnetic_force(pos, m):
    # positions must be sorted
    pos.sort()

    # search space for dist b/w balls
    low, high = 1, pos[-1]-pos[0]
    ans = 0

    while low <= high:
        mid = (low+high)//2 # candidate dist

        if can_place(pos, m, mid):
            ans = mid # dist possible
            low = mid+1 # try larger dist
        else:
            high = mid-1
    
    return ans

def can_place(pos, m, dist):
    count = 1 # fist ball placed
    last = pos[0]

    for p in pos:

        # check if next ball can be placed
        if p-last >= dist:
            count += 1
            last = p
        
        if count >= m:
            return True
        
    return False
