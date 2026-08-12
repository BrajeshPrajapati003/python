'''
Given an array: degree of array = max freq of any element
Find: Smallest contiguous subarray having the SAME degree
Ex: 
    nums = [1, 2, 2, 3, 1]
    freq: 1-> 2, 2 -> 2, 3 -> 1; degree = 2
    smallest subarray having degree 2 = [2, 2] => 2
'''
def findShortestSubarray(nums):

    count = {}
    first = {}

    degree = 0, min_len = 0

    for i, num in enumerate(nums):

        if num not in first:
            first[num] = i

        count[num] = count.get(num, 0) + 1
        freq = count[num]

        if freq > degree:
            degree = freq
            min_len = freq
            min_len = i - first[num] + 1
        
        elif freq == degree:
            min_len = min(min_len, i-first[num] + 1)

    return min_len
