def prefixCountOnes(arr: List, l: int, r: int) -> int:
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        arr[i] = count
    
    if l == 0:
        return arr[r]
    else:
        return arr[r] - arr[l-1]
    
