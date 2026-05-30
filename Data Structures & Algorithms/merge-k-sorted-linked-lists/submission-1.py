# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge_two(self, head1, head2):
        if head1 is None:
            return head2

        if head2 is None:
            return head1
        
        head = None
        next1 = head1.next
        next2 = head2.next

        if head1.val < head2.val:
            head = head1
            head1 = next1
        else:
            head = head2
            head2 = next2
        
        tail = head

        while True:
            if head1 is None and head2 is None:
                return head
            elif head1 is None:
                tail.next = head2
                return head
            elif head2 is None:
                tail.next = head1
                return head

            next1 = head1.next
            next2 = head2.next

            if head1.val < head2.val:
                tail.next = head1
                head1 = next1
            else:
                tail.next = head2
                head2 = next2
            
            tail = tail.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = lists[0]

        for i in range(1, len(lists)):
            head = self.merge_two(head, lists[i])
        
        return head
            