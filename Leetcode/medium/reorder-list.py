""" 
# REORDER LIST

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        parent = None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            parent = slow
            slow = slow.next
            fast = fast.next.next
        
        if not parent:
            return
        parent.next = None
        prev = None
        cur = slow

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        begin = head
        
        while begin and prev:
            temp = begin.next
            temp2 = prev.next
            begin.next = prev
            if temp:
                prev.next = temp
            begin = temp
            prev = temp2