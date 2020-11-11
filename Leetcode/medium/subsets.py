""" 
# SUBSETS

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
] 
"""

def subsets(nums):
    return subset(nums)
    
def subset(nums):
    if len(nums) == 0:
        return []
    
    if len(nums) == 1:
        return [[], nums]
    
    res = []
    x = nums[0]
    t = subset(nums[1:])
    res.extend(t)
    for y in t:
        temp = [x]
        temp.extend(y)
        res.append(temp)                
    return res