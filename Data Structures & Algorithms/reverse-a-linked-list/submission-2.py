# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        if current is None:
            return None

        nnext = head.next

        if nnext is None:
            return head

        current.next = None

        while nnext is not None:
            old_next = nnext.next
            nnext.next = current
            current = nnext
            nnext = old_next
        
        return current