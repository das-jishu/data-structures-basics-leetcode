""" 
# 3SUM CLOSEST

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution. 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4 
"""

def threeSumClosest(nums, target):
    res = nums[0] + nums[1] + nums[2]
    nums = sorted(nums)
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums < target:
                left += 1
            else:
                right -= 1
            if abs(sums - target) < abs(res - target):
                res = sums   
            
    return res