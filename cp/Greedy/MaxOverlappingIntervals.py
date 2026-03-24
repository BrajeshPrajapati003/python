'''
Given intervals = [[start,end],...]
Each interval = airplane in sky
start = takeoff, end = landing
Goal: Max no. of airplanes in sky at any time
'''
def max_airplanes(intervals):

    # store all events (start & end)
    # type: +1 -> start, -1 -> end
    events = [] # [time, type]

    # create events (intervals -> events)
    for s, e in intervals:
        events.append((s, 1)) # start
        events.append((e, -1)) # end

    # sort by time, then type (-1 before +1) because landing happens first
    # if start == end -> we must process end first
    events.sort(key=lambda x:(x[0], x[1])) # this avoids counting false overlaps

    curr = 0
    max_planes = 0

    # traverse events (line sweep)
    for time, val in events:
        curr += val
        max_planes = max(max_planes, curr)

    return max_planes

intervals = [[1, 5], [2, 6], [4, 8], [7, 9]]
print(max_airplanes(intervals)) # 3
