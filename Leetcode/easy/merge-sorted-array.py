""" 
# MERGE SORTED ARRAY

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n 
"""

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
		
        last_idx = 0
        max_num_item = m
        
        for n2 in nums2:
            
            # go as far as n2 can go
            while last_idx < max_num_item and n2 >= nums1[last_idx]:
                last_idx += 1
                
            # shift to right once
            nums1[last_idx + 1:max_num_item +1] = nums1[last_idx:max_num_item]
            
            # insert current value(n2)
            nums1[last_idx]  = n2
            max_num_item += 1