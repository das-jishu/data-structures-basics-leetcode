
def combination(s):
    out = set()
    if len(s) == 1:
        out = set(s)

    for i, word in enumerate(s):
        for p in combination(s[:i] + s[i+1:]):
            out.add(p)
            out.add(''.join(sorted(word + p)))

    return out

if __name__ == "__main__":
    print(sorted(combination("abcd"), key=lambda item: (len(item), item)))