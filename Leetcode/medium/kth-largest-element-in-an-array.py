""" 
# Kth LARGEST ELEMENT IN AN ARRAY

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length. 
"""

# NOT EFFICIENT

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        if len(nums) == 0:
            return 
        
        for i, x in enumerate(nums):
            temp = x
            pos = i
            j = i + 1
            while j < len(nums):
                if nums[j] > temp:
                    temp = nums[j]
                    pos = j
                    
                j += 1
                
            t = nums[pos]
            nums[pos] = x
            nums[i] = t
            
            if k == 1:
                return nums[i]
            
            k -= 1
            
        return nums[0]

# EFFICIENT USING BINARY HEAP

""" class Solution:
       def findKthLargest(self, nums: List[int], k: int) -> int:
           heapq.heapify(nums)
           return heapq.nlargest(k,nums)[-1] """
            