''' 
Split array into k subarrays such that the largest subarray sum is minimized.
'''

# Find the minimum possible largest subarray sum
def split_array(nums, k):

    # no subarray can have sum < max element
    low = max(nums)
    high = sum(nums)
    ans = high  # store best valid answer

    while low <= high:
        mid = (low + high) // 2

        # Check if we can split into <= k subarrays with this max sum
        if canSplit(nums, k, mid):
            ans = mid       # valid answer
            high = mid - 1  # try smaller maximum sum
        else:
            low = mid + 1   # increase allowed sum

    return ans

def canSplit(nums, k, maxSum):
    subarrays = 1   # at least one subarray
    currSum = 0

    for num in nums:
        currSum += num

        # If current subarray exceeds allowed sum
        if currSum > maxSum:
            subarrays += 1  # start a new subarray
            currSum = num   # reset sum

        # If more than k subarrays are needed → not possible
        if subarrays > k:
            return False

    return True
