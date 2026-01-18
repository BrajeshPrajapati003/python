def countVowelsInSubstring(arr: str, l: int, r: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    newArr = []
    count = 0
    for i in range(len(arr)):
        if arr[i] in vowels:
            count += 1
        newArr.append(count)
    
    return newArr[r] if l == 0 else newArr[r] - newArr[l-1]


#IMP Tip: If you were using this in a real app where you query the same string thousands of times, you should move the prefixSum array into a Class field (member variable). That way, you only loop through the string once when you create the object, rather than every time you want to count a range.

