
def rec(target, coins, known):
    min_coins = target
    if target in coins:
        known[target] = 1
        return 1

    elif known[target] > 0:
        return known[target]

    else:
        for i in [c for c in coins if c <= target]:
            num = 1 + rec(target - i, coins, known)
            if num < min_coins:
                min_coins = num
                known[target] = min_coins
    return min_coins

if __name__ == "__main__":
    target = 12
    coins = [1, 4, 8, 10]
    known = [0] * (target + 1)
    print(rec(target, coins, known))