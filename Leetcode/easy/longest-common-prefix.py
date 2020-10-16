""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters. """

def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        n = min([len(x) for x in strs])
        res = ""
        f = 1
        for i in range(n):
            temp = strs[0][i]
            for t in strs:
                if t[i] != temp:
                    f = 0
                    break
            if f == 0:
                break
            else:
                res += strs[0][i]
        return res