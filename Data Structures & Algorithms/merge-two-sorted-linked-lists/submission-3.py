# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()


        # go until one of the lists becomes none then we cut it off early so use and
        # Had the logic right main issue in this case was using or insted of and, 
        # have to use and in tis case becuase both lists have to be none
        while list1 and list2:

            # If list1 val is greater then we put list2 val as next and increment list 2 else otherwise
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next 
                
            else:
                head.next = list1
                list1 = list1.next
            # incrementing head to head.next either way
            head = head.next

        # if one list is longer than the other then append to end of new list
        head.next = list1 or list2

        return dummy.next