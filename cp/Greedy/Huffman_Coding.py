'''
Given: chars = ['a','b','c','d'], freq  = [5, 9, 12, 13]
Goal:
    build a binary tree
    assign binary codes to characters
    minimize total encoding length
Huffman Goal: minimize total bits required to encode data.

frequent -> shorter, Rare -> longer 
Total bits become less.

Depth = code length
if small values go deeper -> cost is small
    so frequent nodes stay near root
if big values go deeper -> cost becomes huge
    so rare nodes go deeper
'''
import heapq

def huffman_coding(freq):
    heap = freq[:]
    heapq.heapify(heap) # add all frequencies

    total_cost = 0

    # combine until one element left
    while len(heap) > 1:
        a = heapq.heappop(heap) # smallest
        b = heapq.heappop(heap) # 2nd smallest

        merged = a + b
        total_cost += merged

        heapq.heappush(heap, merged)
    
    return total_cost

freq = list(map(int, input().split()))
print(huffman_coding(freq)) # 78


# ! “Huffman coding minimizes encoding length by assigning shorter codes to frequent characters using a greedy approach of merging the smallest frequencies first.”
