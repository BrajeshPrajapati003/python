"Minimum Internet Bandwidth (Data Transfer Problem)"
def min_bandwidth(data, hours):
    low, high = 1, max(data)
    ans = high

    while low <= high:
        mid = (low + high) // 2

        time = 0
        for d in data:
            time += (d + mid - 1) // mid

        if time <= hours:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
