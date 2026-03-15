'''
Given:
    items with value & weight.
    a knapsack with max capacity w
Goal: Maximize total value in the knapsack.
(You can take fractions of items)
'''
def fractional_knapsack(values, weights, w):

    # create a list of items with value, weight & ratio
    items = []

    for i in range(len(values)):
        # ratio = value per unit weight
        ratio = values[i]/weights[i]

        items.append((ratio, values[i], weights[i]))

    # sort items in desc order of ratio
    items.sort(reverse=True)

    totalVal = 0

    for ratio, val, wt in items:

        # if we can take the whole item
        if w >= wt:
            w -= wt
            totalVal += val

        else:
            # take fractional part
            totalVal += ratio*w
            break
    
    return int(totalVal)

values = list(map(int, input().split()))
weights = list(map(int, input().split()))
cap = int(input())

print(fractional_knapsack(values, weights, cap))
