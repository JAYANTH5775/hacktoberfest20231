# Minimum number of the coin to geet he required final amount
from collections import defaultdict


def coin_exchange(coins, amount):

    coins.sort(reverse=True)
    print("the coins given is --> "+str(coins))

    final_denomination = defaultdict(int)

    for i in coins:
        while amount >= i:
            final_denomination[i] += 1
            amount -= i
    print(final_denomination)


coin_exchange([1, 2, 5, 10, 20, 50, 100, 500, 1000], 201)


def alternate(coins, amount):

    n = amount

    coins.sort()
    index = len(coins)-1

    while True:
        coinvalue = coins[index]

        if n >= coinvalue:
            print(coinvalue)
            n -= coinvalue
        if n < coinvalue:
            index -= 1

        if n == 0:
            break


coins = [1, 2, 5, 20, 50, 100]

alternate(coins, 201)
