'''
Goal: Find the min no. of jumps needed to reach the last idx.
You are guaranteed that the last idx is reachable.
'''
def jump(nums):

    jumps = 0 # number of jumps taken
    currEnd = 0 # end of current jump range
    farthest = 0 # farthest reachable idx

    # we don't need to process last idx
    # we count the jump that reaches the last idx, not a jump from it
    for i in range(len(nums)-1):

        # can't move further -> unreachable
        if i > farthest:
            return -1

        # update farthest reachable position
        farthest = max(farthest, i+nums[i])

        # if we reach the boundary of curr jump
        if i == currEnd:

            jumps += 1 # make a jump
            currEnd = farthest # update next boundary
    
    return jumps


nums = list(map(int, input().split()))
print(jump(nums))
