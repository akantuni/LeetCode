# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        
        target = l - n + 1

        curr = head
        prev = None
        idx = 1
        while idx != target:
            prev = curr
            curr = curr.next
            idx += 1
        
        if prev is None:
            head = head.next
        else:
            prev.next = curr.next
        
        return head
