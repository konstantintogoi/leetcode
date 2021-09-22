"""
Solution of the easy problem
https://leetcode.com/problems/merge-two-sorted-lists/
"Merge Two Sorted Lists"
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.val is None:
            return '[]'
        vals, node = [self.val], self.next
        while node:
            vals.append(node.val)
            node = node.next
        return repr(vals)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge Two Sorted Lists.

        >>> Solution().mergeTwoLists(
        ...     ListNode(1, ListNode(2, ListNode(4))),
        ...     ListNode(1, ListNode(3, ListNode(4))),
        ... )
        [1, 1, 2, 3, 4, 4]
        >>> Solution().mergeTwoLists(ListNode(None), ListNode(None))
        []
        >>> Solution().mergeTwoLists(ListNode(None), ListNode(0))
        [0]

        """
        if l1.val is None:
            return l2
        if l2.val is None:
            return l1

        l = ListNode()
        root = l

        while l1 and l2:
            node = ListNode()
            if l1.val > l2.val:
                node.val = l2.val
                l2 = l2.next
            else:
                node.val = l1.val
                l1 = l1.next

            l.next = node
            l = node

        while l1:
            node = ListNode(l1.val)
            l.next = node
            l = node
            l1 = l1.next

        while l2:
            node = ListNode(l2.val)
            l.next = node
            l = node
            l2 = l2.next

        return root.next
