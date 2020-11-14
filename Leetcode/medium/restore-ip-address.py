""" 
# RESTORE IP ADDRESS

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
Constraints:

0 <= s.length <= 3000
s consists of digits only.
"""

class Solution:
    def restoreIpAddresses(self, s: str):
        return self.ip(s, 4)
        
    def ip(self, s, n):
        if len(s) < n:
            return []
        
        if n == 1:
            if self.valid(s):
                return [s]
            else:
                return []
        
        result = []
        i = 1
        while i <= 3:
            if self.valid(s[0:i]):
                temp = self.ip(s[i:], n - 1)
                if len(temp) == 0:
                    i += 1
                    continue
                for x in temp:
                    x = s[0:i] + "." + x
                    result.append(x)
            i += 1
        return result
        
    
    def valid(self, s):
        if len(s) == 1:
            return True
        elif 1 < len(s) < 4:
            if s[0] == "0":
                return False
            elif 10 <= int(s) <= 255:
                return True
            else:
                return False
        else:
            return False