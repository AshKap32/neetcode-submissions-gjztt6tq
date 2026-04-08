# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = node = ListNode
        def recurrsive_call(prevs: ListNode, currs: ListNode):
            if not currs:
                return prevs
            temp = currs.next 
            currs.next  = prevs
            return recurrsive_call(prevs= currs, currs= temp)
        return recurrsive_call(prevs=None, currs=head)


        # #Iterative Solution
        # prev, curr = None, head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev
        


        