"""
Solution of the hard problem - "Merge k Sorted Lists",
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.val:
            return '[]'
        vals, node = [self.val], self.next
        while node:
            vals.append(node.val)
            node = node.next
        return repr(vals)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """Merge k Sorted Lists.

        >>> Solution().mergeKLists([
        ...     ListNode(1, ListNode(4, ListNode(5))),
        ...     ListNode(1, ListNode(3, ListNode(4))),
        ...     ListNode(2, ListNode(6))
        ... ])
        [1, 1, 2, 3, 4, 4, 5, 6]

        """
        root = curnode = ListNode(None)

        while curnode and lists:
            im, m = -1, float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val < m:
                    im, m = i, lists[i].val
            curnode.next = lists[im]
            curnode = lists[im]
            lists[im] = curnode.next if curnode else None
            if not lists[im]:
                del lists[im]

        return root.next

