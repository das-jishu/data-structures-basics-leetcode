""" 
# FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109 
"""
class Solution:
    def __init__(self):
        self.result = [-1,-1]
    
    def searchRange(self, nums, target: int):
        self.binary(nums, 0, len(nums) - 1, target)
        return self.result
       
    def binary(self, nums, l, r, target):
        if l > r:
            return
        mid = (l + r) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                self.result[0] = mid
                self.binary(nums, mid + 1, r, target)
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                self.result[1] = mid
                self.binary(nums, l, mid - 1, target)
            if mid != 0 and mid != len(nums) - 1 and nums[mid] == nums[mid - 1] == nums[mid + 1]:
                self.binary(nums, l, mid - 1, target)
                self.binary(nums, mid + 1, r, target)

        elif target < nums[mid]:
            self.binary(nums, l, mid - 1, target)

        else:
            self.binary(nums, mid + 1, r, target)
