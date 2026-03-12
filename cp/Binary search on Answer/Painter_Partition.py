'''
You're given board length boards[] and k painters.
Each painter paints contiguous boards.
Find the minimum time required to paint all boards.
(Assume: 1 unit board = 1 unit time)
'''
def painter_partition(boards, k):
    low, high = max(boards), sum(boards)
    ans = high

    while low <= high:
        mid = (low+high)//2 # candidate time

        if can_paint(boards, k, mid):
            ans = mid # valid time
            high = mid-1 # try smaller time
        else:
            low = mid+1
        
    return ans

def can_paint(boards, k, max_time):
    painters = 1
    curr = 0 # time used by current painter

    for b in boards:
        curr += b

        # if painter exceeds allowed time
        if curr > max_time:
            painters += 1
            curr = b

        # if painters exceed k -> impossible
        if painters > k:
            return False
    
    return True
