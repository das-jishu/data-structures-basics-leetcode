""" 
# MAXIMUM PRODUCT SUBARRAY

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray. 
"""

class Solution:
    def maxProduct(self, nums) -> int:
        
        maxi = nums[0]
        mini = nums[0]
        final = nums[0]
        
        for x in nums[1:]:
            temp = maxi
            maxi = max(max(maxi * x, mini * x), x)
            mini = min(min(temp * x, mini * x), x)
            
            final = max(final, maxi)
            
        return final