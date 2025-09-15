"""
Solution of the medium problem
https://leetcode.com/problems/rotate-list/
"Rotate List"
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
    def rotateRight(
        self, head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        """Return the list rotated to the right by `k` places.

        >>> Solution().rotateRight(
        ...     ListNode(1,
        ...         ListNode(2,
        ...             ListNode(3,
        ...                 ListNode(4,
        ...                     ListNode(5)
        ...                 )
        ...             )
        ...         )
        ...     ),
        ...     2
        ... )
        [4, 5, 1, 2, 3]
        >>> Solution().rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)
        [2, 0, 1]

        """
        if not head:
            return head

        n = 1
        node = head
        while node.next:
            n += 1
            node = node.next

        k = k % n
        node.next = head
        for i in range(n - k):
            node = node.next

        head = node.next
        node.next = None
        return head

