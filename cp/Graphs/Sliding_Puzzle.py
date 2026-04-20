'''
You're given a 2*3 board: [1 2 3], [4 0 5]
where: 
    0 = empty space
    You can swap 0 with adjacent tile (up/down/left/right)
Goal: convert board into: [1 2 3], [4 5 0]
Return: Min number of moves. If impossible -> -1
'''

# Intuition: convert board into string = "123405", target = "123450"
# for indexes: [0 1 2], [3, 4, 5]
# possible swaps: 
#   0 → [1,3], 1 → [0,2,4], 2 → [1,5], 3 → [0,4], 4 → [1,3,5], 5 → [2,4]

# We don't need a graph data structure explicitly,
# but the puzzle itself is an implicit graph of states.

#! Each configuration can transition to several valid next configurations depending on zero’s position, so we model the puzzle as an implicit graph and use BFS for minimum moves.

from collections import deque
def slidingPuzzle(board):

    start = "".join(str(num) for row in board for num in row)
    target = "123450"

    # index -> possible swap positions
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    q = deque([(start, 0)])
    vis = set([start])

    while q:
        state, steps = q.popleft()

        if state == target:
            return steps
        
        zero = state.index('0')

        # generate neighbors
        for nei in moves[zero]:
            arr = list(state)
            arr[zero], arr[nei] = arr[nei], arr[zero] # swap

            new_state = "".join(arr)

            if new_state not in vis:
                vis.add(new_state)
                q.append((new_state, steps+1))

    return -1
