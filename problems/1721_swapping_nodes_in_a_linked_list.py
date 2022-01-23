"""
Solution of the medium problem
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"Swapping Nodes in a Linked List"
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
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """Swap Nodes.

        >>> N = ListNode
        >>> 
        >>> head = N(1, N(2, N(3, N(4, N(5)))))
        >>> Solution().swapNodes(head, 2)
        [1, 4, 3, 2, 5]
        >>> head = N(7, N(9, N(6, N(6, N(7, N(8, N(3, N(0, N(9, N(5))))))))))
        >>> Solution().swapNodes(head, 5)
        [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
        >>> Solution().swapNodes(N(1), 1)
        [1]
        >>> Solution().swapNodes(N(1, N(2)), 1)
        [2, 1]
        >>> Solution().swapNodes(N(1, N(2, N(3))), 2)
        [1, 2, 3]

        """
        root = ListNode(None, head)
        i = 1
        node = root
        while i < k:
            node = node.next
            i += 1
        first = node

        node = node.next
        second = root
        while node.next:
            node = node.next
            second = second.next

        first.next, second.next = second.next, first.next
        first.next.next, second.next.next = second.next.next, first.next.next

        return root.next
