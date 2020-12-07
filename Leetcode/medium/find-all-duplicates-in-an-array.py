""" 
# FIND ALL DUPLICATES IN AN ARRAY

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3] 
"""

# Using cyclic sorting

class Solution:
    def findDuplicates(self, nums):
        
        i = 0
        while i < len(nums):
            id = nums[i] - 1
            
            if nums[id] != id + 1:
                t = nums[id]
                nums[id] = nums[i]
                nums[i] = t
                
            else:
                i += 1
                
        return [v for i, v in enumerate(nums) if v != i + 1]