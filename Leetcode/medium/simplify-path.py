""" 
# SIMPLIFY PATH

Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period '.' refers to the current directory. Furthermore, a double period '..' moves the directory up a level.

Note that the returned canonical path must always begin with a slash '/', and there must be only a single slash '/' between two directory names. The last directory name (if it exists) must not end with a trailing '/'. Also, the canonical path must be the shortest string representing the absolute path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:

Input: path = "/a/./b/../../c/"
Output: "/c"
 
Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid Unix path. 
"""

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