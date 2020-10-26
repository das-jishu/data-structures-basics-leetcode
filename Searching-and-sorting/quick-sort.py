
def q_s(arr):
    quick_sort(arr, 0, len(arr) - 1)

def quick_sort(arr, first, last):
    if first < last:
        pos = split(arr, first, last)
        quick_sort(arr, first, pos - 1)
        quick_sort(arr, pos + 1, last)

def split(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            done = True

        else:
            t = arr[left]
            arr[left] = arr[right]
            arr[right] = t

    t = arr[right]
    arr[right] = arr[first]
    arr[first] = t

    return right

if __name__ == "__main__":
    arr = [3, 2, 7, 6, 1, 0, 4, 8, 2]
    q_s(arr)
    print(arr)