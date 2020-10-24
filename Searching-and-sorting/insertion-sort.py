
def insertion_sort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        x = i - 1
        while x >= 0 and arr[x] > el:
            arr[x + 1] = arr[x]
            x -= 1

        arr[x + 1] = el

if __name__ == "__main__":
    arr = [7, 3, 5, 6, 3, 1, 0, 8, 3]
    arr2 = [3, 1]
    insertion_sort(arr)
    insertion_sort(arr2)
    print(arr2)
    print(arr)
