""" 
# SEARCH IN ROTATED SORTED ARRAY II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why? 
"""

class Solution:
    def search(self, nums, target: int):
        pivot=0
        for ar in range(len(nums)-1):
            if nums[ar]>nums[ar+1]:
                pivot=ar+1
                break
        nums = nums[pivot:]+nums[0:pivot]
        left=0
        right=len(nums)-1
        while left<=right:
            mid = int((left+right)/2)
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False