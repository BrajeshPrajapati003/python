def sumFromLtoR(arr: List, l: int, r: int) -> int:
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    
    if l == 0:
        return arr[r]
    else:
        return arr[r]-arr[l-1]
    
