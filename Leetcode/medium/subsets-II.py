""" 
# SUBSETS II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
] 
"""

def subsetsWithDup(nums):
    return subsets(sorted(nums))
    
def subsets(nums):
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [[], nums]

    res = []
    x = nums[0]
    t = subsets(nums[1:])
    #res.extend(t)
    for g in t:
        if g not in res:
            res.append(g)
    for y in t:
        temp = [x]
        temp.extend(y)
        if temp not in res:
            res.append(temp)                
    return res