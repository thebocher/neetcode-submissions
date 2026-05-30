# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_head = None
        current_tail = None
        
        if list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current_head = list1
                list1 = list1.next
            else:
                current_head = list2
                list2 = list2.next
            
            current_tail = current_head
        elif list1 is not None:
            return list1
        elif list2 is not None:
            return list2
        else:
            return None
        
        while True:
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    current_tail.next = list1
                    list1 = list1.next
                else:
                    current_tail.next = list2
                    list2 = list2.next
            elif list1 is not None:
                current_tail.next = list1
                list1 = list1.next
            elif list2 is not None:
                current_tail.next = list2
                list2 = list2.next
            else:
                return current_head
            
            if current_tail.next is not None:
                current_tail = current_tail.next


            
