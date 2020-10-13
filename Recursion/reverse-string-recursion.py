
def reverse(s):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

if __name__ == "__main__":
    print(reverse('hello'))
    print(reverse('h'))
    print(reverse('true lies'))