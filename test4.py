
# declaring collatz() method
def collatz(n) -> None:
    # print(1) if n is 1 and stop
    if n == 1:
        print(1)
    # if n is even, print n and call method recursively by n / 2
    elif n % 2 == 0:
        print(n)
        collatz(n // 2)
    # if n is odd, print n and call method recursively with 3*n+1
    else:
        print(n)
        collatz(3 * n + 1)

collatz(5)
