
def solve(n, k, arr):
    m = 0
    i = 0
    while i < n - 2:
        t = k
        j = i + 1
        while j < n - 1 and t > 0:
            t -= arr[j] - arr[i]
            j += 1

        m = max(m, j-i)
        i += 1
    return m

print(solve(3,1,[1,2,3]))