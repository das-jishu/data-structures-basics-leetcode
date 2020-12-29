""" 
# PALINDROME LINKED LIST

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space? 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        parent = None
        cur = head
        while cur != slow:
            temp = cur.next
            cur.next = parent
            parent = cur
            cur = temp
            
        if fast and not fast.next:
            slow = slow.next
            
        while parent:
            if parent.val != slow.val:
                return False
            parent = parent.next
            slow = slow.next
            
        return True
            
            
        