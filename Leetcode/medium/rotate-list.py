""" 
# ROTATE LIST

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL 
"""

def rotateRight(head, k: int):
        
    if not head or not head.next:
        return head
    
    prev = head
    cur = head.next
    
    count = 2
    while cur.next != None:
        prev = cur
        cur = cur.next
        count += 1
        
    k = k % count
    prev = None
    front = head
    end = head
    if k == 0:
        return head
    
    while k > 1:
        end = end.next
        k -= 1
        
    while end.next != None:
        prev = front
        front = front.next
        end = end.next
        
    prev.next = None
    end.next = head
    head = front
    
    return head