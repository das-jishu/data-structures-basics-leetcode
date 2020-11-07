""" 
# PERMUTATIONS

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
] 
"""

def permute(nums):
    if len(nums) == 1:
        return [nums]
    
    result = []
    for i, x in enumerate(nums):
        y = permute(nums[:i] + nums[i+1:])
        for t in y:
            t.append(x)
            result.append(t)
            
    return result