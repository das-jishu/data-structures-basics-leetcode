""" 
# SHORTEST UNSORTED CONTINUOUS SUBARRAY

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0

Constraints:

1 <= nums.length <= 104
-10^5 <= nums[i] <= 10^5 
"""

# inefficient. Takes O(N^2) time. For O(N) time and O(1) space, check leetcode

class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        
        i = 0
        start = 0
        end = 0
        while i < len(nums) - 1:
            t = min(nums[i+1:])
            if t < nums[i]:
                start = i
                break
            i += 1
            
        i = len(nums) - 1
        while i >= 1:
            t = max(nums[:i])
            if t > nums[i]:
                end = i
                break
            i -= 1
        
        length = end - start + 1
        if end == 0 and start == 0:
            length = 0
        
        return length
            
            
                
            