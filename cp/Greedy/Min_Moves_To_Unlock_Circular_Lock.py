'''
Given: lock = "1234", target = "3456"
Each wheel:
    can rotate forward (9->0)
    can rotate backward (0->9)
Goal: min moves to convert lock -> target
'''
def min_moves(lock, target):
    moves = 0

    for i in range(len(lock)):
        a = int(lock[i])
        b = int(target[i])

        diff = abs(a-b)

        # choose shorted circular path (0->9 = 10)
        moves += min(diff, 10-diff)
    
    return moves

print(min_moves("1234", "3456")) # 8
