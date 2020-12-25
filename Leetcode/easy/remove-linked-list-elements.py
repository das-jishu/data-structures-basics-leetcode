""" 
# REMOVE LINKED LIST ELEMENTS

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        parent = None
        start = head
        
        while start:
            if start.val == val:
                if not parent:
                    head = start.next
                else:
                    parent.next = start.next
                
            else:
                parent = start
                
            start = start.next
            
        return head