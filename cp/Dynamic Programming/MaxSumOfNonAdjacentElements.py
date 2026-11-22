def subsequencesSum(arr):
    # return subsequencesSumRecursion(arr, len(arr)-1)
    # dp = [-1]*len(arr), dp[0] = arr[0]
    # return subsequencesSumMemoization(arr, dp, len(arr)-1)
    return subsequencesSumConstantSpace(arr)

def subsequencesSumRecursion(arr, idx):
    if idx == 0:
        return arr[idx]
    
    if idx < 0:
        return 0

    pick = arr[idx] + subsequencesSumRecursion(arr, idx-2)
    skip = subsequencesSumRecursion(arr, idx-1)

    return max(pick, skip)

def subsequencesSumMemoization(arr, dp, idx):
    if idx == 0:
        return arr[idx]
    if idx < 0:
        return 0

    if dp[idx] != -1:
        return dp[idx]
    
    pick = arr[idx] + subsequencesSumMemoization(arr, dp, idx-2)
    skip = subsequencesSumMemoization(arr, dp, idx-1)
    dp[idx] = max(pick, skip)
    
    return dp[idx]

def subsequencesSumTabulation(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    dp = [0]*len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        skip = dp[i-1]
        pick = arr[i] + dp[i-2]

        dp[i] = max(pick, skip)
    
    return dp[n-1]

def subsequencesSumConstantSpace(arr):
    n = len(arr)
    if n < 1:
        return 0
    if n == 1:
        return arr[0]
    
    prev2, prev1 = arr[0], max(arr[0], arr[1])
    for i in range(2, n):
        pick = prev2 + arr[i]
        skip = prev1

        curr = max(pick, skip)

        prev2 = prev1
        prev1 = curr

    return prev1

arr = list(map(int, input().split()))
print(subsequencesSum(arr))
