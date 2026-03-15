'''
Given 2 arrays:
    gas[i] -> gas available at station i
    cost[i] -> gas needed to travel to next station.
You start with an empty tank.
Goal: Find the stating gas station idx from which you can complete the full circle.
'''
def canCompleteCircle(gas, cost):

    # total gas vs total cost check
    if sum(gas) < sum(cost):
        return -1
    
    tank = 0
    start = 0

    for i in range(len(gas)):

        # gas gained at this station
        tank += gas[i]-cost[i]

        # if tank becomes -ve
        if tank < 0:

            # next station becomes new start
            start = i+1
            tank = 0 # reset tank

    return start

gas = list(map(int, input().split()))
cost = list(map(int, input().split()))
print(canCompleteCircle(gas, cost))
