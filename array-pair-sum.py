
def pair_sum(li, sum):
    """ 
    APPROACH USING DICTIONARY
    
    count = {}
    k = 0
    for x in li:   
        count[k] = x
        k += 1
    
    print(type(count.values()))
    result = []
    for x in count.values():
        if (sum - x) in count.values():
            print('Found: [',x,' ',(sum-x),']')
            result.append([x, sum - x])

    return len(result) // 2 """

    # USING SET
    # EDGE CASES
    if (len(li) < 2):
        return

    seen = set()
    output = set()

    for num in li:
        t = sum - num
        if t not in seen:
            seen.add(num)

        else:
            output.add((t, num))

    return output

if __name__ == "__main__":
    print(pair_sum([1, 3, 2, 2, 6, 2, 5, 4], 7))
    print(pair_sum([1, 5, 3, 3], 6))