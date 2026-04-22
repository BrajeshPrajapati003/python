'''
You're given bus routes: routes[i] = stops covered by bus i
Need min. buses from src stop to target stop.

Input: 
    routes = [[1, 2, 7], [3, 6, 7]]
    src = 1, target = 6
Output: 2 (bus0: 1 -> 7, bus1: 7 -> 6)
'''
from collections import defaultdict, deque

def numBusesToDestination(routes, src, target):

    if src == target:
        return 0
    
    # map: stop -> buses
    stop_to_buses = defaultdict(list)

    for i, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].append(i)

    q = deque()
    vis_buses = set()

    # start with all buses that have src stop
    for bus in stop_to_buses[src]:
        q.append((bus, 1)) # (bus, buses taken)
        vis_buses.add(bus)

    while q:
        bus, steps = q.popleft()

        # check all stops this bus visits
        for stop in routes[bus]:

            # if target == stop
            if stop == target:
                return steps
            
            # go to all buses from this step
            for next_bus in stop_to_buses[stop]:
                if next_bus not in vis_buses:
                    vis_buses.add(next_bus)
                    q.append((next_bus, steps+1))
    
    return -1
