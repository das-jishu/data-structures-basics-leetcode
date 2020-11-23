""" 
# FIND PEAK ELEMENT

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity. 
"""

class Solution:
    def findPeakElement(self, nums) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        return self.findPeak(1, len(nums) - 2, nums)
        
    def findPeak(self, left, right, nums):
        if left > right:
            return None
        mid = (left + right) // 2
        """
        print("left:",left,"right:",right,"mid:",mid)
        print("leftitem:",nums[mid-1],"rightitem:",nums[mid+1],"miditem:",nums[mid])
        """
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid - 1
        
        return self.findPeak(mid + 1, right, nums) or self.findPeak(left, mid - 1, nums)