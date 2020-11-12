""" 
# REMOVE DUPLIACTES FROM SORTED LIST

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # dummy takes care of duplicates at the beginning
        dummy = ListNode(float('inf'), head)
        head = dummy
        parent = head
        front = head.next
        
        flag = False
        while front and parent.next:

            # to adjust for duplicates at the end
            if not front.next and flag:
                parent.next = None
                break

            # duplicates at the middle
            elif front.next and front.val == front.next.val:
                front = front.next
                # found duplicates so setting flag
                flag = True

            # reached an unique element    
            else:
                # if duplicates were found in the earlier iteration
                if flag:
                    front = front.next
                    flag = False

                # if no duplicates in earlier iteration
                else:
                    parent.next = front
                    parent = front
                    front = front.next
                    
        return head.next