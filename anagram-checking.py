
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    count = {}

    for x in s1:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    for x in s2:
        if x in count:
            count[x] -= 1
        else:
            return False

    for k in count:
        if count[k] != 0:
            return False

    return True

if __name__ == "__main__":
    print(anagram('Hey gg', 'yeH kg'))
    print(anagram('Clint Eastwood', 'Old West Action'))
    print(anagram('Coffee', 'Co ff ee'))
    print(anagram('dddddd', 'eeeeee'))
    
