# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        if fast is None:
            return False

        while True:
            fast = fast.next and fast.next.next
            slow = slow.next

            if fast is None:
                return False

            if fast == slow:
                return True

