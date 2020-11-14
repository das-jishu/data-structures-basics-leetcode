""" 
# REVERSE LINKED LIST II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        parent = None
        front = head
        end = head.next
        count = 1
        while end != None:
            if count != m:
                parent = front
                front = end
                end = end.next
                count += 1
                continue
            else:
                break
        
        while count < n and end != None:
            temp = end.next
            end.next = front
            front = end
            end = temp
            count += 1
        
        if not parent:
            head.next = end
            head = front
        else:
            parent.next.next = end
            parent.next = front
            
        return head