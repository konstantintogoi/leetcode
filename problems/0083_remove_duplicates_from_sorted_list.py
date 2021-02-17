"""
Solution of "Remove Duplicates from Sorted List" problem at
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Remove Duplicates.

        >>> Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(2))))
        [1, 2]
        >>> Solution().deleteDuplicates(
        ...     ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        ... )
        [1, 2, 3]

        """
        node = head
        while node:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head

