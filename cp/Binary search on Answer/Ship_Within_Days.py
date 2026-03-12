'''
Your are given a number of package weights & a number of days D.
You must ship packages in order. Each day you load packages until the ship capacity is reached.
Find the minimum ship capacity so all packages are delivered within D days.
'''
def ship_within_days(weights, days):
    low, high = max(weights), sum(weights)
    ans = high

    while low <= high:

        # candidate ship capacity
        mid = (low + high) // 2

        d = 1       # number of days required
        curr = 0    # current load for the day

        for w in weights:
            curr += w

            # if capacity exceeded → start new day
            if curr > mid:
                d += 1
                curr = w

        # if we can ship within allowed days
        if d <= days:
            ans = mid       # valid answer
            high = mid - 1  # try smaller capacity
        else:
            low = mid + 1   # increase capacity

    return ans
