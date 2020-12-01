""" 
# CONTAINS DUPLICATE III 

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

Constraints:

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1 
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if t == 0:
            return self.containsNearbyDuplicate(nums, k)
        else:
            for i in range(len(nums)):
                n1 = nums[i]
                sub_list = nums[i+1:i+k+1]
                for n2 in sub_list:
                    if abs(n1-n2) <= t:
                        return True
            return False
                    
        
    def containsNearbyDuplicate(self, nums, k):
        for i,v in enumerate(nums):
            if nums.count(v) > 1:
                if v in nums[i+1:i+k+1]:
                    return True
        return False