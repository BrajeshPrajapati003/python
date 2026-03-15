'''
Your are given arrival & departure time of trains.
Each time is in HHMM format.
Find the minimum number of platforms needed so that no train waits.
'''
def minPlatforms(arr, dep):
    # sort arrival & departure times
    arr.sort(); dep.sort()

    # pointer for arrival & departure array
    i = j = 0

    # current platforms needed
    platforms = 0

    # max platforms needed at any time
    maxPlatforms = 0

    while i<len(arr) and j<len(dep):
        if arr[i] <= dep[j]:
            platforms += 1 # needed one more platform
            maxPlatforms = max(platforms, maxPlatforms)
            i += 1 # move to next arrival
        else:
            platforms -= 1 # train departed, free one platform
            j += 1 # move to next departure

    return maxPlatforms

arr = list(map(int, input().split()))
dep = list(map(int, input().split()))

print(minPlatforms(arr, dep))