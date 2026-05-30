# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while True:
            fast = fast.next and fast.next.next
            slow = slow.next

            if fast is None:
                break
        
        rhalf = slow
        
        if not slow:
            return 

        rhalf_tail = slow.next
        rhalf.next = None

        while True:
            if rhalf_tail is None:
                break

            nnext = rhalf_tail.next
            rhalf_tail.next = rhalf
            rhalf = rhalf_tail
            rhalf_tail = nnext
        
        while True:
            if rhalf is None:
                head.next = None
                break
            elif head.next == rhalf:
                break
                                
            head_next = head.next
            head.next = rhalf

            rhalf_next = rhalf.next
            rhalf.next = head_next

            rhalf = rhalf_next
            head = head_next

        
        

            
