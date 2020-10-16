""" 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros. 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = head = ListNode()
        carry = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
            if l2:
                b = l2.val
            sum = a + b + carry
            if sum < 10:
                carry = 0
            else:
                sum -= 10
                carry = 1
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
            res.next = ListNode(sum)
            res = res.next
        if carry == 1: 
            res.next = ListNode(1)
        return head.next