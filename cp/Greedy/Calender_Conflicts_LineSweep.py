'''
Given: intervals = [[start, end],...]
Each meeting needs a room
Meetings overlap -> need more rooms
Goal: Min number of rooms required
'''
def min_rooms(intervals):

    # convert to events
    events = []
    for s, e in intervals:
        events.append((s, 1)) # start
        events.append((e, -1)) # end
    
    # sort events by time, then type (end first, then start)
    events.sort(key=lambda x:(x[0],x[1]))

    curr = 0
    max_rooms = 0

    # sweep (curr += val & track max)
    for _, val in events:
        curr += val
        max_rooms = max(max_rooms, curr)

    return max_rooms

print(min_rooms([[0,30],[5,10],[15,20]])) # 2
