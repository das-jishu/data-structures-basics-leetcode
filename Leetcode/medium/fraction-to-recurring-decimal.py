""" 
# FRACTION TO RECURRING DECIMAL

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0 
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        pos = False
        if numerator * denominator >= 0:
            pos = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        quot = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            if pos:
                return (str)(quot)
            else:
                return "-" + (str)(quot)
            
        frac = ""
        rem = []
        i = -1
        while True:
            remainder *= 10
            q = remainder // denominator
            frac += str(q)
            if remainder in rem:
                i = rem.index(remainder)
                break
            rem.append(remainder)
            remainder = remainder % denominator
            if remainder == 0:
                break
        
        res = ""
        if i == -1:
            res = str(quot) + "." + frac
        else:
            res = str(quot) + "." + frac[:i] + "(" + frac[i:-1] + ")"
         
        print(pos)
        if pos == False:
            res = "-" + res
            
        return res