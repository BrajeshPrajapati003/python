'''
You're given a 2*3 board: [1 2 3], [4 0 5]
where: 
    0 = empty space
    You can swap 0 with adjacent tile (up/down/left/right)
Goal: convert board into: [1 2 3], [4 5 0]
Return: Min number of moves. If impossible -> -1
'''
import collections
from typing import List

def slidingPuzzle(board: List[List[int]]) -> int:
    start = "".join(str(num) for row in board for num in row)
    target = "123450"

    neighbors = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4],
        4: [1,3,5],
        5: [2,4]
    }

    q = collections.deque([start])
    visited = {start}
    steps = 0

    while q:
        for _ in range(len(q)):
            state = q.popleft()

            if state == target:
                return steps

            zero = state.index('0')

            for nei in neighbors[zero]:
                new_state = list(state)
                new_state[zero], new_state[nei] = new_state[nei], new_state[zero]
                new_state = "".join(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    q.append(new_state)

        steps += 1

    return -1
