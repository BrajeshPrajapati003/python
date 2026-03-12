'''
Given machines[] where each values is time taken by a machine to produce one item.
Find the minimum time needed to produce goal items.
'''
def min_time(machines, goal):
    low = 1 # min time = 1
    high = min(machines) * goal
    # max time = fastest or slowest machine producing all items
    # high = max(machines)*goal or min(machines)*goal
    # min(machines)*goal is better as it's a much tighter bound

    # max(machines)*goal -> larger value -> slower binary search
    # min(machines)*goal -> smaller value -> faster binary search

    ans = 0

    while low <= high:
        mid = (low+high) // 2

        products = 0

        # calculate products made in 'mid' time
        for m in machines:
            products += mid // m
        
        if products >= goal:
            ans = mid
            high = mid-1
        else:
            low = mid+1
        
    return ans

