""" 
# PERMUTATIONS II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10 
"""

class Solution:
    def __init__(self):
        self.result = []
        
    def permuteUnique(self, nums):
        nums.sort()
        self.result = self.permute(nums)
        return self.result
    
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        result = []
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            y = self.permute(nums[:i] + nums[i+1:])
            for t in y:
                t.append(x)
                result.append(t)

        return result