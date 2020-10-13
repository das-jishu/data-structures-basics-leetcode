
def permutations(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):
            for perm in permutations(s[:i] + s[i+1:]):
                print(perm)
                out += [let + perm]

    return out

if __name__ == "__main__":
    print(permutations('abc'))