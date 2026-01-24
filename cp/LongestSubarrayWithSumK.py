class Solution:

    # Length of the longest subarray with sum = k
    def longestSubarraySumK(arr: List, k: int) -> int:
        map = {0:-1}
        maxLen = 0
        for i in range(len(arr)):
            sum += arr[i]
            if (sum-k) in map:
                len = i-map[sum-k]
                if(maxLen < len):
                    maxLen = len
            if sum not in map:
                map[sum] = i
        
        return maxLen


    # Longest subarray with sum = k
    def findLargestSubarrayWithSumK(arr: List, k: int) -> List[int]:
        map = {0: -1}
        maxLen = 0
        start, end = -1, -1
        sum = 0
        
        for i in range(len(arr)):
            sum += arr[i]
            if (sum-k) in map:
                len = i-map[sum-k]
                if(len > maxLen):
                    maxLen = len
                    start = map[sum-k] + 1
                    end = i
                
            if sum not in map:
                map[sum] = i
            
        return arr[start: end+1]