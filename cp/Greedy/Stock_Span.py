'''
Given daily stock prices: prices = [100, 80, 60, 70, 60, 75, 85]
For each day, find how many consecutive days before it (including today)
where price <= today's price
output: [1, 1, 1, 2, 1, 4, 6]
'''
def stock_span(prices):
    n = len(prices)
    span = [0]*n
    # stack stores last greater element to the left
    stack = [] # store indices

    for i in range(n):

        # pop all smaller or equal elements
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

        # if stack empty -> no greater element on left
        if not stack:
            span[i] = i+1
        else:
            span[i] = i-stack[-1]

        stack.append(i)
    
    return span

prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))
