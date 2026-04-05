'''
Given: rooms[i] = list of keys inside room i
each key = access to another room
Goal: Can you visit all rooms starting from room 0?
'''
from collections import deque

def canVisitAllRooms(rooms):
    n = len(rooms)
    vis = [False]*n

    q = deque([0])
    vis[0] = True

    while q:
        node = q.popleft()

        for key in rooms[node]:
            if not vis[key]:
                vis[key] = True
                q.append(key)
    
    return all(vis)
