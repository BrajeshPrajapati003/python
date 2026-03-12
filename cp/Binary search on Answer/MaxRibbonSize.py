'''
Given ribbon lengths ribbons[], cut them to obtain exactly k ribbons of equal length.
Find the maximum possible ribbon length.
'''
def max_ribbon_size(ribbons, k):
    low, high = 1, max(ribbons)
    ans = 0

    while low <= high:
        mid = (low+high)//2

        count = 0
        for r in ribbons:
            count += r // mid
        
        if count >= k:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    
    return ans
