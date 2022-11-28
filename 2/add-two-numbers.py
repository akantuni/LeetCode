# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            digit = (v1 + v2) % 10
            carry = (v1 + v2) // 10

            if carry > 0:
                if l1.next:
                    l1.next.val += carry
                else:
                    l1.next = ListNode(carry)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            cur.val = digit
            if l1 or l2:
                cur.next = ListNode()
                cur = cur.next

        return ans
