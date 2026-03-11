"Minimum machine processing speed"
def min_machine_speed(tasks, hours):
    low, high = 1, max(tasks)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        time = 0
        for t in tasks:
            time += (t + mid - 1) // mid

        if time <= hours:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
