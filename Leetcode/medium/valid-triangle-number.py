""" 
# VALID TRIANGLE NUMBER

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000]. 
"""

class Solution:
    def triangleNumber(self, nums) -> int:
        result = 0
        nums.sort()
        
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = i + 2
            if nums[i] == 0:
                i += 1
                continue
            while j < len(nums) - 1:
                if nums[j] == 0:
                    j += 1
                    continue
                while k < len(nums) and nums[k] < nums[i] + nums[j]:
                    k += 1
                result += k - j - 1
                j += 1
                
            i += 1
            
        
        return result