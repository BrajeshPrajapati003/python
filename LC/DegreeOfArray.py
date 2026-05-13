'''
Given an array: degree of array = max freq of any element
Find: Smallest contiguous subarray having the SAME degree
Ex: 
    nums = [1, 2, 2, 3, 1]
    freq: 1-> 2, 2 -> 2, 3 -> 1; degree = 2
    smallest subarray having degree 2 = [2, 2] => 2
'''
def findShortestSubarray(nums):

    freq = {}
    first = {}
    last = {}

    for i, num in enumerate(nums):

        freq[num] = freq.get(num, 0) + 1

        if num not in first:
            first[num] = i
        
        last[num] = i
    
    degree = max(freq.values())

    ans = len(nums)

    for num in freq:
        if freq[num] == degree:
            length = last[num] - first[num] + 1
            ans = min(ans, length)
    
    return ans

print(findShortestSubarray(list(map(int, input().split(",")))))
