""" 
# SWAP NODES IN PAIRS

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]
 
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100 
"""

def swapPairs(head):
    if head == None or head.next == None:
        return head
    
    parent, front = None, head
    back = head.next
    res = back
    
    while back and front:
        temp = back.next
        if parent:
            parent.next = back
        back.next = front
        front.next = temp
        
        parent = front
        front = parent.next
        if front != None:
            back = parent.next.next
            
    return res