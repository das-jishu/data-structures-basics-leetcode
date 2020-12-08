""" 
# SUBARRAY SUM EQUALS K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 10^7
"""

class Solution:
    # Sliding window solution but doesn't work for some negative values

    """def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum = 0
        i, j = 0, 0
        c = 0
        while j < len(nums):
            print("i:",i,"j:",j,"sum:",sum)
            if sum + nums[j] > k:
                if i >= j:
                    j += 1
                    continue
                sum -= nums[i]
                i += 1
                
            elif sum + nums[j] == k:
                c += 1
                sum += nums[j]
                j += 1
                
            else:
                sum += nums[j]
                j += 1
            
        return c"""
    
    # works for all

    def subarraySum(self, nums, k: int) -> int:
        # Use defaultdict
        map = {}
        map[0] = 1
        
        count, sum = 0, 0
        for num in nums:
            sum += num
            count += map[sum - k]
            map[sum] += 1
        
        return count