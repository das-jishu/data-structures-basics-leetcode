
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for start in range(gap):
            insertion_sort_gap(arr, start, gap)
        gap = gap // 2

def insertion_sort_gap(arr, start, gap):

    i = start + gap
    while i < len(arr):
        target = arr[i]
        j = i - gap
        while j >= 0 and arr[j] > target:
            arr[j + gap] = arr[j]
            j -= gap
        arr[j + gap] = target
        i += gap

if __name__ == "__main__":
    arr = [3, 4, 2, 6, 5, 1, 0, 2]
    arr2 = [3, 1]
    shell_sort(arr)
    shell_sort(arr2)
    print(arr)
    print(arr2)
