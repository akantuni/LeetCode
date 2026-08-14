# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            d = ListNode()
            curr = d

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next

            if list1:
                curr.next = list1
            else:
                curr.next = list2

            return d.next
        
        def helper(lists):
            if len(lists) == 0:
                return
            elif len(lists) == 1:
                return lists[0]
            elif len(lists) == 2:
                return merge(lists[0], lists[1])

            return merge(helper(lists[:len(lists) // 2]), helper(lists[len(lists) // 2:]))

        return helper(lists)
