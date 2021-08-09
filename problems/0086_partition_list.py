"""
Solution of the medium problem - "Partition List",
https://leetcode.com/problems/partition-list/
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        """Partition List.

        >>> Solution().partition(
        ...     ListNode(1,
        ...     ListNode(4,
        ...     ListNode(3,
        ...     ListNode(2,
        ...     ListNode(5,
        ...     ListNode(2,
        ... )))))), 3)
        [1, 2, 2, 4, 3, 5]
        >>> Solution().partition(ListNode(2, ListNode(1)), 2)
        [1, 2]

        """
        lefthead = ListNode(None)
        righthead = ListNode(None)

        left = lefthead
        right = righthead
        node = head

        while node:
            if node.val < x:
                left.next = node
                left = node
            else:
                right.next = node
                right = node

            node = node.next

        left.next = righthead.next
        right.next = None

        return lefthead.next

