
''' Longest Substring without repeating characters '''

def longestSubstringWithoutRepeatingChar(s: str):
    st = set()
    l = 0
    maxLen = start = 0

    for r in range(len(s)):
        
        # shrink window until duplicate is removed
        while s[r] in st:
            st.remove(s[l])
            l += 1
        
        # now safe to add
        st.add(s[r])

        # update max len if better
        if r-l+1 > maxLen:
            maxLen = r-l+1
            start = l
    
    print(s[start: start+maxLen])

# longestSubstringWithoutRepeatingChar(input())

#####################################################

''' Kadane's Algo '''

def maxSubarraySum(nums: list[int]):
    curr = maxSum = nums[0]

    for i in range(1, len(nums)):
        curr = max(curr+nums[i], nums[i]) # restart or extend
        maxSum = max(curr, maxSum)
    
    print(maxSum)

# maxSubarraySum(list(map(int, input().split())))

#####################################################

'''Rotate array by k steps '''

def rotateKSteps(nums: list[int], k: int):
    k %= len(nums)

    nums[:] = nums[-k:] + nums[:-k]

    ans = " ".join(list(map(str, nums)))
    print(ans)

# rotateKSteps(list(map(int, input().split())), int(input()))

#####################################################

''' merge 2 sorted arrays '''

def merge2SortedArrays(nums1: list[int], nums2: list[int]):

    res = []
    i = j = 0
    n1 = len(nums1)
    n2 = len(nums2)

    while i<n1 and j<n2:

        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1

    # while i<n1:
    #     res.append(nums1[i])
    #     i+=1
    #     k+=1
    
    # while j<n2:
    #     res.append(nums2[j])
    #     j+=1
    #     k+=1

    res.extend(nums1[i:])
    res.extend(nums2[j:])

    print(" ".join(map(str, res)))

# merge2SortedArrays(list(map(int, input().split())), list(map(int, input().split())))

''' find duplicate element (1 to N array)'''
# Given an array of size n+1 containing numbers from 1 to n, find the duplicate number.

def findDuplicate(nums: list[int]):
    slow = fast = nums[0]

    # detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # find entry point
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    print(slow)

# findDuplicate(list(map(int, input().split())))

#####################################################

''' intersection of 2 arrays - common unique elements present in both '''

def intersection(a: list[int], b: list[int]):

    ans = list(set(a) & set(b))
    print(" ".join(map(str, ans)))

# intersection(list(map(int, input().split())), list(map(int, input().split())))

#####################################################

''' leaders in array '''
# leader = greater than all elements to its right

def leadersInArray(arr: list[int]):

    res = []
    maxNum = float('-inf')
    for num in reversed(arr):
        if num > maxNum:
            res.append(num)
            maxNum = num
    
    res = res[::-1]
    print(" ".join(map(str, res)))

# leadersInArray(list(map(int, input().split())))

#####################################################

''' stock buy and sell (max profit)'''

def maxProfit(prices):
    
    minPrice = float('inf')
    profit = 0

    for p in prices:
        minPrice = min(minPrice, p)
        profit = max(profit, p-minPrice)
    
    print(profit)

# maxProfit(list(map(int, input().split())))

#####################################################

''' check rotation of string - one string is rotation of another string'''

def isRotation(s1: str, s2: str):
    ans = (len(s1) == len(s2) and s2 in (s1 + s2))
    print(ans)

# isRotation(input(), input())

#####################################################

''' spiral matrix traversal - clockwise'''

def spiralMatrix(mat: list[list[int]]):

    res = []
    top, bottom = 0, len(mat)-1
    left, right = 0, len(mat[0])-1

    while top <= bottom and left <= right:
        # left -> right
        for i in range(left, right+1):
            res.append(mat[top][i])
        top += 1

        # top -> bottom
        for i in range(top, bottom+1):
            res.append(mat[i][right])
        right -= 1

        # right -> left
        for i in range(right, left-1, -1):
            res.append(mat[bottom][i])
        bottom -= 1

        # bottom -> top
        for i in range(bottom, top-1, -1):
            res.append(mat[i][left])
        left += 1
    
    print(res)

# n = int(input())
# mat = list([map(int, input().split)] for _ in range(n))
# spiralMatrix(mat)

#####################################################

''' transpose of matrix '''

def transposeMatrix(mat: list[list[int]]):
    n = len(mat); m = len(mat[0])
    res = [[0]*m for _ in range(n)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i][j] = mat[j][i]
    
    print(res)

#####################################################

''' count subarrays with given sum '''

def countSubarraySumK(nums: list[int], k: int):
    count = 0
    preSum = 0
    map = {0: 1}
    for num in nums:
        preSum += num


        if preSum-k in map:
            count += map[preSum-k]
        
        map[preSum] = map.get(preSum, 0) + 1
    
    print(count)

#####################################################

''' convert binary to decimal '''

''' convert decimal to binary '''

''' convert decimal to n-base format '''


