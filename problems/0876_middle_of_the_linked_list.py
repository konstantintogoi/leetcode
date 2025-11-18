"""
Solution of the easy problem
https://leetcode.com/problems/middle-of-the-linked-list/
"Middle of the Linked List"
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Return the middle node of the linked list.

        >>> Solution().middleNode(
        ... ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        ... )
        [3, 4, 5]
        >>> Solution().middleNode(
        ...     ListNode(1, ListNode(2, ListNode(3,
        ...         ListNode(4, ListNode(5, ListNode(6)))
        ...     )))
        ... )
        [4, 5, 6]

        """
        n = 1 if head else 0
        node = head

        while node and node.next:
            node = node.next
            n += 1

        i = 1
        mid = n // 2 + 1
        node = head

        while i < mid:
            node = node.next
            i += 1

        return node

