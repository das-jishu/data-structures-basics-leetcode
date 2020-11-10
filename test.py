def simplifyPath(path: str) -> str:
        
    if len(path) == 1:
        return "/"
    
    res = "/"
    path = path[1:]
    if path[-1] != "/":
        path += "/"
    temp = ""
    for x in path:
        if x != "/":
            temp += x
            continue
        else:
            print("res:",res,"temp:", temp)
            if temp == "" or temp == ".":
                pass
            elif temp == "..":
                if res == "/":
                    pass
                else:
                    t = len(res) - 2
                    while True:
                        if res[t] != "/":
                            res = res[:t]
                            t -= 1
                        else:
                            t -= 1
                            break
            else:
                res += temp + "/"
            temp = ""
            
    if len(res) > 2 and res[-1] == "/":
        res = res[:len(res) - 1]
        
    return res

if __name__ == "__main__":
    print(simplifyPath("/a//b////c/d//././/.."))