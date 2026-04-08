# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Have to track the nodes we've visited and its next, so theoretically could 
        # make a map that has a key of the node and the value can be pointed to the node that is after


        visited_map = set()
        curr = head

        while curr:
            if curr in visited_map:
                return True
            visited_map.add(curr)
            curr = curr.next
        return False

           
