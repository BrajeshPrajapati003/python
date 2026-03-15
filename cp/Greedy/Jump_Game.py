'''
Given:
    An array, each value represents the max jump length from that idx.
Goal: Determine if you can reach the last idx.
'''
def canJump(nums):

    # max idx we can reach so far
    maxReach = 0
    for i in range(len(nums)):

        # if curr idx is beyond reachable range
        if i > maxReach:
            return False
        
        # update farthest reachable idx
        maxReach = max(maxReach, i+nums[i])
    
    return True

print(canJump(list(map(int, input().split()))))
