# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            curr_next = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            curr.next = prev.next
            prev.next = curr

            curr = curr_next
        
        return dummy.next