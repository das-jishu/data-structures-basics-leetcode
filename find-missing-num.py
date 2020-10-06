
def missing(arr1, arr2):
    count = {}
    for num in arr2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in arr1:
        if num not in count:
            return num
        else:
            count[num] -= 1

if __name__ == "__main__":
    print(missing([1, 2, 3, 5, 6, 9, 8, 2, 2, 4], [2, 2, 4, 2, 1, 3, 5, 6, 8]))