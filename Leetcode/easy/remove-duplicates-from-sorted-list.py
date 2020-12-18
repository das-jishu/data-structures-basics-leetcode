""" 
# REMOVE DUPLICATES FROM SORTED LIST

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = head
        while temp != None and temp.next != None:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                    continue
            
                temp = temp.next
                    
        return head