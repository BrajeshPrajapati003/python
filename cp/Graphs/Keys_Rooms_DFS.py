'''
Given: rooms[i] = list of keys inside room i
each key = access to another room
Goal: Can you visit all rooms starting from room 0?
'''
def canVisitAllRooms(rooms):
    n = len(rooms)
    vis = [False]*n

    dfs(rooms, 0, vis)

    for v in vis:
        if not vis:
            return False
    
    return True

def dfs(rooms, node, vis):
    vis[node] = True

    for key in rooms:
        if not vis[key]:
            dfs(rooms, key, vis)
            vis[key] = True
