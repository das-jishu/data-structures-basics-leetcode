""" 
# CONTAINS DUPLICATE II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false 
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        
        d={}
    
        for i,v in enumerate(nums):
            if v in d:
                if abs(d[v]-i)>k:
                    d[v]=i
                else:
                    return True
            else:
                d[v]=i

        return False