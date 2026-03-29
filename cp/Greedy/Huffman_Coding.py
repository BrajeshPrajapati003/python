'''
Given: chars = ['a','b','c','d'], freq  = [5, 9, 12, 13]
Goal:
    build a binary tree
    assign binary codes to characters
    minimize total encoding length
'''
import heapq

def huffman_coding(freq):
    heap = freq[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        merged = a + b
        total_cost += merged

        heapq.heappush(heap, merged)
    
    return total_cost

freq = list(map(int, input().split()))
print(huffman_coding(freq)) # 78
