class Solution:
    def countFreqOfX(arr: List, x: int, l: int, r: int) -> int:
        count = 0
        newArr = []
        for i in range(len(arr)):
            if arr[i] == x:
                count += 1
            newArr.append(count)
        
        return newArr[r] if l == 0 else newArr[r]-newArr[l-1]

