''' Koko_Eating_Bananas '''
import math

# Binary search range for K (bananas per hour)
def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    ans = high  # store minimum valid speed

    while low <= high:
        mid = (low + high) // 2  # candidate eating speed

        # Check if Koko can finish within h hours with this speed
        if canEat(piles, h, mid):
            ans = mid    # valid speed, try smaller
            high = mid - 1
        else:
            low = mid + 1  # speed too slow, increase

    return ans

# Calculate total hours needed if Koko eats k bananas/hour
def canEat(piles, h, k):
    hours = 0

    for p in piles:
        # ceil division because partial pile still takes 1 hour
        hours += math.ceil(p / k)
        # or: hours += (p + k - 1) // k

    return hours <= h
