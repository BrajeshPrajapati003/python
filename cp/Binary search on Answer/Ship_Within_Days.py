'''
Your are given a number of package weights & a number of days D.
You must ship packages in order. Each day you load packages until the ship capacity is reached.
Find the minimum ship capacity so all packages are delivered within D days.
'''
def ship_within_days(weights, days):
    low, high = max(weights), sum(weights)
    ans = high

    while low <= high:
        mid = (low+high)//2

        if canShip(weights, days, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def canShip(weights, days, capacity):
    d = 1
    curr = 0
    for w in weights:
        if curr+w > capacity:
            d += 1
            curr = w
        else:
            curr += w
    
    return d <= days
