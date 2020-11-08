def checkAnagram(s1, s2):
    d = {}
    for x in s1:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    print(d)    
    for x in s2:
        if x not in d or d[x] == 0:
            return False
        else:
            d[x] -= 1
    print(d)  
    for x in d:
        if d[x] != 0:
            return False
        
    return True

if __name__ == "__main__":
    print(checkAnagram("dee", "eed"))