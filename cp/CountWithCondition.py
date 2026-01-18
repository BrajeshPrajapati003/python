def countEvenLessThanX(arr: List, x: int, l: int, r: int) -> int:
    count = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i]&1 == 0 and arr[i] <= x:
            count += 1
        newArr.append(count)
    
    if l == 0:
        return newArr[r]
    else:
        return newArr[r]-newArr[l-1]



def countOddLargerThanX(arr: List, x: int, l: int, r: int) -> int:
    count = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i]&1 != 0 and arr[i]>x:
            count += 1
        newArr.append(count)
    
    if l == 0:
        return newArr[r]
    else:
        return newArr[r] - newArr[l-1]



# In Python, you cannot assign to an index of an empty list like newArr[i] = count if that index doesn't exist yet. You would need to use newArr.append(count) or initialize the list first.

