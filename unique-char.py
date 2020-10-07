
def uniq(s):
    c = {}
    for x in s:
        if x not in c:
            c[x] = 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(uniq("ddeadrghrfj"))
    print(uniq("dhiren"))
    print(uniq("monke"))
    print(uniq("derd"))