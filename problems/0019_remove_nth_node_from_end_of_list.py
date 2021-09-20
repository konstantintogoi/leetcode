"""
Solution of the medium problem
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"Remove Nth Node From End of List"
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Remoth Nth Node.

        >>> Solution().removeNthFromEnd(
        ...     ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ...     2
        ... )
        [1, 2, 3, 5]
        >>> Solution().removeNthFromEnd(ListNode(1), 1)
        >>> Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1)
        [1]
        >>> Solution().removeNthFromEnd(
        ...     ListNode(1, ListNode(2, ListNode(3, ListNode(4,
        ...     ListNode(5, ListNode(6, ListNode(7, ListNode(8,
        ...     ListNode(9, ListNode(10)))))))))), 7
        ... )
        [1, 2, 3, 5, 6, 7, 8, 9, 10]

        """
        node, sz = head, 0
        while node:
            sz += 1
            node = node.next

        if n == sz:
            return head.next

        node, i = head, 1
        while node:
            if i == sz - n and node.next:
                node.next = node.next.next
            i += 1
            node = node.next

        return head
