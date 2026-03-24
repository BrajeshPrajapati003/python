'''
Given: n candies with prices arr[]
Offer: for every 1 candy you buy, you can get at most k other candies free
Goal: find min & max cost.
'''
def candy_store(arr, k):
    arr.sort()
    n = len(arr)

    minCost = 0
    i = 0
    j = n-1

    while i<n and j>=0:
        minCost += arr[i]
        i+=1
        j-=k
    
    maxCost = 0
    i = 0
    j = n-1

    while i<n and j>=0:
        maxCost += arr[j]
        i+=k
        j-=1

    return list((minCost, maxCost))

arr = list(map(int, input().split()))
k = int(input())
res = " ".join(map(str, candy_store(arr,k)))
print(res)
