# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case = once there is no other var left ( bottom of the list)
        if not head or not head.next:
            return head
        
        # recurrsively call until we are at the bottom of the list
        new_head = self.reverseList(head.next)

        next_val = head.next

        # Setting the next value head to the current head value
        next_val.next = head
        # setting the current head next to none
        head.next = None

        # returns end of list value
        return new_head
