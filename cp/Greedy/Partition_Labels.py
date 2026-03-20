'''
Given: s = "ababcbacadefegdehijhklij"
Partition the string into as many parts as possible such that:
    each letter appears in at most one part
Return the sizes of partitions
'''
def partitionLabels(s):
    # store last occurrence of each character
    last = {}
    for i, ch in enumerate(s):
        last[ch] = i
    
    res = []
    start = end = 0

    # traverse string
    for i, ch in enumerate(s):

        # extend partition boundary
        end = max(end, last[ch])

        # if current idx reaches boundary -> partition ends
        if i == end:
            res.append(end-start+1)
            start = i+1 # start next partition
        
    return res

s = input()
print(partitionLabels(s))
