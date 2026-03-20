'''
Given: num = "1432219", k = 3
Remove k digits such that the resulting no. is min. possible.
'''
def remove_k_digits(num, k):
    stack = []

    for digit in num:

        # remove larger previous digits
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # if k still remains -> remove from end
    # the stack is monotonically increasing (non-decreasing)
    # In an increasing sequence, largest digits are at the end
    while k > 0:
        stack.pop()
        k -= 1
    
    res = "".join(stack) # build result
    res = res.lstrip('0') # remove leading zeroes

    return res if res else "0"

s = input()
k = int(input())
print(remove_k_digits(s, k))
