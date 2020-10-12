
def check(phrase, li, output=None):
    if output == None:
        output = []

    for word in li:
        if phrase.startswith(word):
            output.append(word)
            return check(phrase[len(word):], li, output)

    return output

if __name__ == "__main__":
    print(check("ilovedogs", ["i", "dogs", "love", "man"]))
    print(check("ilovedogs", ["ice", "dogs", "love", "man"]))