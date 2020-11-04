""" # 4 SUM

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [], target = 0
Output: []

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109 
"""

def fourSum(nums, target):
    result = []
    if len(nums) < 4:
        return result
    
    nums.sort()
    
    for i in range(len(nums) - 3):
        if not (i > 0 and nums[i] == nums[i - 1]):
            val = threeSum(nums[i+1:], target - nums[i])
            if len(val) != 0:
                for g in val:
                    temp = g + [nums[i]]
                    result.append(temp)
                        
    return result

def threeSum(num, tar):
    res = []
    if len(num) < 3:
        return []
    num = sorted(num)
    for i, t in enumerate(num):
        if not (i > 0 and num[i] == num[i - 1]):
            val = twoSum(num[i+1:], tar - t)
            if len(val) != 0:
                for g in val:
                    temp = list(g) + [t]
                    res.append(temp)

    return res

def twoSum(arr, value):
    s = set()
    output = set()
    for x in arr:
        if (value - x) not in s:
            s.add(x)
        else:
            output.add((x, value - x)) 
    return output