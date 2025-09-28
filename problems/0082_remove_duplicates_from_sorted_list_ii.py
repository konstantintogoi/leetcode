"""
Solution of the medium problem
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"Remove Duplicates from Sorted List II"
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Delete all nodes that have duplicate numbers.

        >>> Solution().deleteDuplicates(
        ...     ListNode(1,
        ...         ListNode(2,
        ...             ListNode(3, ListNode(3,
        ...                 ListNode(4, ListNode(4,
        ...                     ListNode(5)
        ...                 ))
        ...             ))
        ...         )
        ...     )
        ... )
        [1, 2, 5]
        >>> Solution().deleteDuplicates(
        ...     ListNode(1, ListNode(1, ListNode(1,
        ...     ListNode(2,
        ...     ListNode(3)
        ... )))))
        [2, 3]

        """
        head = ListNode(-1, head)
        node = head

        while node:
            duplicate = False
            while node.next and node.next.next and node.next.val == node.next.next.val:
                node.next.next = node.next.next.next
                duplicate = True

            if node.next and duplicate:
                node.next = node.next.next
            else:
                node = node.next

        return head.next

