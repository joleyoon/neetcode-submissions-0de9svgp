# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummy = ListNode()
            curr = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            
            if head1:
                curr.next = head1
            if head2:
                curr.next = head2
            
            return dummy.next

        def divide(lists, left, right):
            if left >= right:
                return lists[left]
            
            middle = (left + right) // 2

            l1 = divide(lists, left, middle)
            l2 = divide(lists, middle + 1, right)

            return merge(l1, l2)
        
        if not lists: return None
        if len(lists) == 1: return lists[0]

        return divide(lists, 0, len(lists) - 1)

        
        





