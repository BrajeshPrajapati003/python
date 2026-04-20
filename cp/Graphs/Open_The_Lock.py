'''
You've a lock: 0000
Each wheel can rotate: 0 <-> 1 <-> 2 ... .. 9
Given: deadends -> forbidden states, target -> desired lock state
Goal: Min. turns needed to reach target. If impossible -> -1

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
'''

# Treat each lock combination as a graph node and use BFS to find minimum turns while avoiding deadends.

#! BFS guarantees the minimum turns because it explores all states reachable in k moves before exploring states reachable in k+1 moves.

from collections import deque
def openLock(deadends, target):

    dead = set(deadends)

    # start blocked
    if "0000" in dead:
        return -1
    
    q = deque([("0000", 0)]) # (state, steps)
    vis = set(["0000"])

    while q:
        state, steps = q.popleft()

        if state == target: # target found
            return steps

        # generate 8 neighbors # +1 & -1 (2 rotations) for each wheel
        for i in range(4): # len(state)
            
            digit = int(state[i])

            for move in [-1, 1]: # rotations

                new_digit = (digit + move) % 10

                new_state = state[:i] + str(new_digit) + state[i+1:]

                if new_state not in dead and new_state not in vis:
                    vis.add(new_state)
                    q.append((new_state, steps+1))
    
    return -1
