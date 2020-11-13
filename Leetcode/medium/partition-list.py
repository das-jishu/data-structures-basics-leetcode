"""
# PARTITION LIST

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        parent = None
        cur = head
        while cur:
            if cur.val >= x:
                break
            else:
                parent = cur
                cur = cur.next
                
        while cur:
            if cur.next and cur.next.val < x:
                temp = cur.next
                cur.next = temp.next or None
                if not parent:
                    temp.next = head
                    head = temp
                    parent = temp
                else:
                    temp.next = parent.next
                    parent.next = temp
                    parent = temp
                
                
            else:
                cur = cur.next or None
                
        return head