
def selection_sort(arr):

    for i in range(len(arr)):
        pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        t = arr[pos]
        arr[pos] = arr[i]
        arr[i] = t

if __name__ == "__main__":
    arr = [2, 6, 4, 6, 7, 1, 0]
    arr2 = [3, 1]
    selection_sort(arr)
    selection_sort(arr2)
    print(arr)
    print(arr2)
    