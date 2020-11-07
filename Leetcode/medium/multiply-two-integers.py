""" 
# MULTIPLY

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself. 
"""

def multiply(num1: str, num2: str) -> str:
    result = "0"
    k = 0
    for x in num2[::-1]:
        """
        # MULTIPLYING IN BRUTE FORCE

        res = ""
        carry = 0
        for y in num1[::-1]:
            t = (int(x) * int(y)) + carry
            res = str(t % 10) + res
            carry = t // 10
        
        if carry > 0:
            res = str(carry) + res
        """

        res = str(int(x) * int(num1))
        res += "0" * k
        k += 1
        
        result = str(int(res) + int(result))
        
        """
        # ADDING IN BRUTE FORCE

        m = max(len(res), len(result))
        carry2 = 0
        s = ""
        while m > 0:
            a, b = 0, 0
            if len(result) == 0:
                a = 0
            else:
                a = int(result[-1])
                result = result[:-1]
            if len(res) == 0:
                b = 0
            else:
                b = int(res[-1])
                res = res[:-1]
            temp = a + b + carry2
            carry2 = temp // 10
            s = str(temp % 10) + s
            m -= 1
        if carry2 > 0:
            s = str(carry2) + s
        result = str(int(s)
        """
        
    return result