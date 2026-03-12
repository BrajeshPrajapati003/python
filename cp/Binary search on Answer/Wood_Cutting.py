'''
Given wood lengths wood[], cut them into pieces of equal length.
Find the maximum piece length so that at least k pieces can be obtained.
'''
def max_piece_length(wood, k):
    low, high = 1, max(wood)
    ans = 0

    while low <= high:
        mid = (low+high)//2 # candidate piece length

        pieces = 0
        
        # count how many pieces we can get
        for w in wood:
            pieces += w // mid

        if pieces >= k:
            ans = mid # possible length
            low = mid+1 # try larger piece
        else:
            high = mid-1
        
    return ans
