""" 
# 3 SUM PROBLEM

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets. 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
 
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(nums):
    result = []
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    for i, t in enumerate(nums):
        if not (i > 0 and nums[i] == nums[i - 1]):
            val = search(nums[i+1:], -t)
            if len(val) != 0:
                for g in val:
                    temp = list(g) + [t]
                    result.append(temp)
            
    return result

def search(arr, value):
    s = set()
    output = set()
    for x in arr:
        if (value - x) not in s:
            s.add(x)
        else:
            output.add((x, value - x)) 
    return output