""" 
# REMOVE NTH NODE FROM END OF LINKED LIST

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        front = head
        parent = None
        end = head
        while n != 0:
            end = end.next
            n -= 1
            
        while end != None:
            end = end.next
            parent = front
            front = front.next
        
        if parent == None:
            return head.next
        parent.next = front.next
        return head
        