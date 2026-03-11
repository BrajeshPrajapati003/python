'''
Problem:
Place K cows in stalls such that the minimum distance between any two cows
is maximized.

Idea:
- Sort the stall positions.
- Use binary search on the answer (distance).
- For each candidate distance, check if we can place k cows.
'''
def aggressive_cows(stalls, k):

    stalls.sort() # dist. should be meaningful
    low = 1 # min possible dist
    high = stalls[-1] - stalls[0] # max possible dist
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        # Check if we can place cows with at least 'mid' distance
        if canPlace(stalls, k, mid):
            ans = mid       # store valid distance
            low = mid + 1   # try larger distance
        else:
            high = mid - 1  # reduce distance

    return ans


def canPlace(stalls, k, dist):

    # Place first cow in the first stall
    cows = 1
    last = stalls[0]

    # Try placing remaining cows greedily
    for i in range(1, len(stalls)):

        # If distance condition satisfied, place cow
        if stalls[i] - last >= dist:
            cows += 1
            last = stalls[i]

        # If all cows placed successfully
        if cows >= k:
            return True

    return False
