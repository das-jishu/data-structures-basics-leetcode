
def bubble_sort(arr):

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


if __name__ == "__main__":
    arr = [3, 6, 2, 5, 0, 5, 2, 9, 7]
    arr2 = [3, 1]
    bubble_sort(arr)
    print(arr)
    bubble_sort(arr2)
    print(arr2)
