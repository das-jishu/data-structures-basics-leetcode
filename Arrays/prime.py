c = 1
for x in range(2, 100):
    flag = True
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            flag = False
            break
    if flag:
        print(c, ": ", x, sep="")
        c += 1
