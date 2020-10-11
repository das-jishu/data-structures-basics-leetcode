
def large(arr):
    if (len(arr)) < 0:
        return 0

    max_sum = current = arr[0]
    for num in arr[1:]:
        current = max(current + num, num)
        max_sum = max(current, max_sum)

    return max_sum

if __name__ == "__main__":
    print(large([1, -1, 3, -4, 5, -3, 6, -3, 2, -1]))