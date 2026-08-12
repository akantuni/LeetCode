# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def idk(head):
            if head is None or head.next is None:
                return
            curr = head.next
            prev = head
            while curr.next:
                curr = curr.next
                prev = prev.next
            
            prev.next = None
            curr.next = head.next
            head.next = curr
            idk(curr.next)

        idk(head)
