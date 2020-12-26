""" 
# COUNT PRIMES

Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0
 
Constraints:

0 <= n <= 5 * 106 
"""

class Solution:
    def countPrimes(self, n):
        nums = [True] * n

        i = 2
        while i * i < n:
            if nums[i]:
                j = 2
                while j * i < n:
                    nums[j * i] = False
                    j += 1

            i += 1

        prime_count = 0
        for n in nums[2:]:
            if n:
                prime_count += 1

        return prime_count