""" 
# MAJORITY ELEMENT

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2 
"""

class Solution:
    def majorityElement(self, nums) -> int:
        
        candidate = nums[0]
        count = 0
        
        for x in nums:
            if candidate == x:
                count += 1
                
            else:
                if count != 0:
                    count -= 1
                else:
                    candidate = x
                    count = 0
                    
        return candidate