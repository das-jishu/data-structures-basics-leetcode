""" 
# PARTITION EQUAL SUBSET SUM

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution1:
    """
    Resursive Solution
    """
    def canPartition(self, nums) -> bool:
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        self.memory = dict()
        
        target = total // 2
        possible = self.select(target, len(nums)-1, nums)
        return possible
    def select(self, target, n, nums):
        if target == 0:
            return True
        if n < 0 or target < 0 :
            return False

        if (target,n) in self.memory:
            return self.memory[(target,n)]
        
        if nums[n] > target:
            ans = self.select(target, n - 1, nums)
        else:
            ans = self.select(target - nums[n], n-1, nums) or self.select(target, n-1, nums)
            
        self.memory[(target,n)] = ans
        return ans
