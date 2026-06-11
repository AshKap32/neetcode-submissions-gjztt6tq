# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
            # Can iterate over and put values into an array and use a two pointer approach
            # it seems like the left value stayes, then the end value comes in
        curr = head
        node_arr = []
        while curr:
            node_arr.append(curr)
            curr = curr.next

        # Becuase we know left then points to right and right next is then left,
        # We can do a two pointer approach with left and right using index access for O(1) access.
        left, right = 0, len(node_arr) - 1

        while left < right:
            # settting the 0th left to right most node
            node_arr[left].next = node_arr[right]
            left += 1

            node_arr[right].next = node_arr[left]
            right -= 1


        # This is because in either case left was set as either the last node, so if it was None then right next is none, if it was an actual node, then we set to none
        node_arr[left].next = None
        


            

