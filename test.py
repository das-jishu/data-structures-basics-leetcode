
def mincoins(target, coins, known):
    # min_coins = target
    res = []
    if target in coins:
        known[target] = [target]
        return [target]

    elif known[target] != None:
        return known[target]

    else:
        for i in [c for c in coins if c <= target]:
            x = mincoins(target - i, coins, known)
            res += [x, i]
            known[target] = res
    return res

if __name__ == "__main__":
    print(mincoins(10, [5, 3], [None]*11))