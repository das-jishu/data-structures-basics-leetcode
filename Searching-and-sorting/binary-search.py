
def binary_search_iter(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

def binary_search_rec(arr, target):
    left, right = 0, len(arr)
    if len(arr) < 1:
        return False

    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        binary_search_rec(arr[:mid], target)
    else:
        binary_search_rec(arr[mid + 1:], target)

    return False


if __name__ == "__main__":
    print(binary_search_iter([1, 2, 3, 4, 5, 6], 5))
    print(binary_search_iter([1, 2, 5, 6], 8))
    print(binary_search_rec([1, 2, 5, 6], 3))
    print(binary_search_rec([1, 2, 5, 6], 5))
    
    
    