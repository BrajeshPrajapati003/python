'''
You're given activities with start & end times.
You can only perform one activity at a time.
Goal: find max. number of activities that can be performed.
'''
def max_activities(start, end):

    # pair start & end
    activities = list(zip(start, end))

    # sorting based on ending time
    activities.sort(key=lambda x: x[1])

    # pick 1st activity after sorting
    count = 1
    # end time of last selected activity
    last_end = activities[0][1]

    # check remaining activities
    for s, e in activities[1:]:
        if  s >= last_end:
            last_end  = e
            count += 1
    
    return count

start = list(map(int, input().split()))
end = list(map(int, input().split()))

print(max_activities(start, end))
