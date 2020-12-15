""" 
# COUNT NUMBERS WITH UNIQUE DIGITS

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
 

Constraints:

0 <= n <= 8 
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        
        prod = 81
        factor = 8
        result = 91
        previous = 91
        k = 3
        while k <= n:
            prod *= factor
            factor -= 1
            previous = result
            result = previous + prod
            k += 1
        
        return result