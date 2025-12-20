"""
Solution of the medium problem
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
"Delete Nodes From Linked List Present in Array"
"""
from typing import List, Optional


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
    def modifiedList(
        self,
        nums: List[int],
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        """Return the `head` of the modified linked list
        after removing all nodes from the linked list that have a value
        that exists in nums.

        >>> Solution().modifiedList(
        ...     [1, 2, 3],
        ...     ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),
        ... )
        [4, 5]
        >>> Solution().modifiedList(
        ...     [1],
        ...     ListNode(1, ListNode(2, ListNode(1,
        ...     ListNode(2, ListNode(1, ListNode(2)
        ...     )))))
        ... )
        [2, 2, 2]
        >>> Solution().modifiedList(
        ...     [5],
        ...     ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ... )
        [1, 2, 3, 4]

        """
        snums = set(nums)

        while head.val in snums:
            head = head.next

        node = head

        while node and node.next:
            while node.next and node.next.val in snums:
                node.next = node.next.next
            node = node.next if node else node

        return head

