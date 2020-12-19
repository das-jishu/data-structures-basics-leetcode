
def longestPalindrome(s):
    count = [0]*26
    for x in s:
        count[ord(x) - 97] += 1

    res = ""
    middle = ""
    for i,x in enumerate(count):
        if x == 0:
            continue
        if x % 2 != 0 and middle == "":
            middle = chr(97 + i)
        res += chr(97 + i) * (x // 2)

    if middle == "":
        res += res[::-1]
    else:
        res = res + middle + res[::-1]

    return res

if __name__ == "__main__":
    print(longestPalindrome("ssaadsbccb"))
    