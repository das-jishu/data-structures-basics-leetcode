""" 
# NEXTPERMUTATION

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100 
"""

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    i = len(nums) - 2
    while i >= 0:
        if nums[i] >= nums[i + 1]:
            i -= 1
            continue
        else:
            pos = i + 1
            mini = nums[i + 1]
            pos2 = i + 1
            while pos < len(nums):
                if nums[pos] < mini and nums[pos] > nums[i]:
                    mini = nums[pos]
                    pos2 = pos
                pos += 1
            
            t = nums[i]
            nums[i] = nums[pos2]
            nums[pos2] = t
            
            nums[i+1:] = sorted(nums[i+1:])
            return
        
    nums.sort()
    return