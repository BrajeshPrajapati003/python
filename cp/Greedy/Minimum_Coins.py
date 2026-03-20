'''
Given: coins[], target amount
You can use infinite coins. 
Find min number of coins to make the amount.
'''
def min_coins_greedy(coins, amt):
    
    # always try largest denomination first
    coins.sort(reverse=True)
    total_coins = 0

    for coin in coins:

        # if current coin can be used
        if amt >= coin:

            # find how many times we can use this coin
            used = amt // coin
            total_coins += used

            amt -= used * coin # reduce remaining amt

    return total_coins if amt == 0 else -1

coins = list(map(int, input().split()))
amt = int(input())

print(min_coins_greedy(coins, amt))
