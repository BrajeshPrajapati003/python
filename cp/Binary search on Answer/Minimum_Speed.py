"Minimum speed to complete tasks"
def min_speed(tasks, h):
    low = 1
    high = max(tasks)
    ans = high
    while low <= high:
        mid = (low+high)//2
        if canFinish(tasks, h, mid):
            ans = mid
            high = mid-1 # try smaller speed
        else:
            low = mid+1 # try higher speed

    return ans

def canFinish(tasks, h, speed):
    hours = 0
    for t in tasks:
        hours += (t + speed - 1)//speed # math.ceil(t/speed)

    return hours <= h

tasks = list(map(int, input().split()))
h = int(input())
print(min_speed(tasks, h))
