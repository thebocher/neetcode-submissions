# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for _ in range(n):
            first = first.next
        
        if first is None:
            if n == 1:
                return None
            
            return second.next
        
        while first.next is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head

        