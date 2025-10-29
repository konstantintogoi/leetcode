"""
Solution of the easy problem
https://leetcode.com/problems/reverse-linked-list/
"Reverse Linked List"
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Return the reversed list.

        >>> Solution().reverseList(
        ... ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        ... )
        [5, 4, 3, 2, 1]
        >>> Solution().reverseList(ListNode(1, ListNode(2)))
        [2, 1]
        >>> Solution().reverseList(None)

        """
        vals = []

        node = head
        while node:
            vals.append(node.val)
            node = node.next

        node = head
        while node:
            node.val = vals.pop()
            node = node.next

        return head

