'''
Given: ratings[i] of children standing in a line
Rules:
    Each child must get at least 1 candy
    If a child has higher rating than neighbor, they must get more candies
Goal: Minimize total candies.
'''
def min_candies(ratings):
    n = len(ratings)

    # each child has 1 candy initially
    candies = [1]*n

    # left -> right (candies[i-1]+1)
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1

    # right -> left (max(candies[i], candies[i+1]+1))
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            # don't overwrite smaller valid ones: take max
            candies[i] = max(candies[i], candies[i+1]+1)
        
    return sum(candies)

ratings = list(map(int, input().split()))
print(min_candies(ratings))
