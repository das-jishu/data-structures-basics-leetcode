
def rev(str):
    rever = temp = ""
    str = str.strip() + " "
    for x in str:
        if x != " ":
            temp += x
        else:
            rever = temp + " " + rever
            temp = ""

    return rever

if __name__ == "__main__":
    print(rev("This is my dream"))
    print(rev("   Hey son  "))