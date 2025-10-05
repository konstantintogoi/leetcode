"""
Solution of the medium problem
https://leetcode.com/problems/reverse-linked-list-ii/
"Reverse Linked List II"
"""
from typing import Optional


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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int,
    ) -> Optional[ListNode]:
        """Return the reversed list.

        >>> Solution().reverseBetween(
        ...     ListNode(1,
        ...         ListNode(2,
        ...             ListNode(3,
        ...                 ListNode(4,
        ...                     ListNode(5)
        ...                 )
        ...             )
        ...         )
        ...     ),
        ... 2, 4)
        [1, 4, 3, 2, 5]
        >>> Solution().reverseBetween(ListNode(5), 1, 1)
        [5]

        """
        vals = []

        node = head
        i = 1 if head else 0
        while node and i < left:
            node = node.next
            i += 1

        while node and i <= right:
            vals.append(node.val)
            node = node.next
            i += 1

        nvals = len(vals)

        node = head
        i = 1 if head else 0
        while node and i < left:
            node = node.next
            i += 1

        while node and i <= right:
            node.val = vals[nvals - (i - left) - 1]
            node = node.next
            i += 1

        return head

