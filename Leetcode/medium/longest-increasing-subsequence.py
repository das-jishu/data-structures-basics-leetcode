""" 
# LONGEST INCREASING SUBSEQUENCE

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
Follow up:

Could you come up with the O(n2) solution?
Could you improve it to O(n log(n)) time complexity? 
"""

class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums)==1:
            return 1   
        dp=[1]*(len(nums))
        ans=0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],1+dp[j])
                ans=max(ans,dp[i])
        return ans

# The above solution is inefficient. Find the efficient algorithm of time O(NlogN)