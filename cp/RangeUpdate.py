# offline range updates + final array -> diff array
def range_update(n, queries):
    diff = [0] * (n+1)

    for l, r, val in queries:
        diff[l] += val
        if r+1 < len(diff):
            diff[r+1] -= val
        
    res = []
    curr = 0
    for i in range(n):
        curr += diff[i]
        res.append(curr)
    
    return res

