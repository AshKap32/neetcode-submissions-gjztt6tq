# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1 = dummy2 = head 

        # no head? return head
        if not head:
            return head
        
        # If the size of the list s = 2 grab sz by iterating over the list
        sz = 0
        while dummy2:
            sz += 1
            dummy2 = dummy2.next
        if sz <= 2:
            remove = sz - n
            if remove == 1:
                head.next = None
            if remove == 0:
                prev = head
                head = head.next
                prev.next = None
            return head

        # iterate till we get to the nth node
        i = 0
        curr = head
        remove = sz - n
        if remove == 0:
            return head.next

        for i in range(remove):
            if i != remove-1:
                curr = curr.next
                continue
            else:
                prev = curr

                print(f"prev: {curr.val}")

                curr = curr.next
                prev.next = curr.next

                print(f"remvoing: {curr.val}")

                curr.next = None
        
        return dummy1
