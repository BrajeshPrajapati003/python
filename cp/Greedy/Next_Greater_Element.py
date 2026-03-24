'''
Given: arr = [4, 5, 2, 10]
For each element, find the next greater element to its right
If none -> -1
'''
def next_greater(arr):
    n = len(arr)
    res = [-1]*n

    # stack to delay decisions until a greater element appears
    stack = [] # stores indices as we need position to update the ans array
    # it's storing "who is waiting for answer"

    for i in range(n):

        # resolve elements in stack
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = arr[i]

        stack.append(i)
    
    return res

arr = [4, 5, 2, 10]
print(next_greater(arr)) # [5, 10, 10, -1]
