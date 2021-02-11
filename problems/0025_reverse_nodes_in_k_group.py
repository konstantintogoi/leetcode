"""
Solution of "Reverse Nodes in k-Group" problem at
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(node.val)
            node = node.next
        return repr(vals)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """Reverse Nodes.

        >>> Solution().reverseKGroup(
        ... ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
        ... )
        [2, 1, 4, 3, 5]
        >>> Solution().reverseKGroup(
        ... ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3
        ... )
        [3, 2, 1, 4, 5]
        >>> Solution().reverseKGroup(
        ... ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1
        ... )
        [1, 2, 3, 4, 5]
        >>> Solution().reverseKGroup(ListNode(1), 1)
        [1]

        """
        if k == 1:
            return head

        ptrs = [head]
        for i in range(k - 1):
            ptrs.append(ptrs[i].next)
        root = ptrs[-1]

        while len(ptrs) == k:
            ptrs[0].next = ptrs[-1].next
            for i in range(k - 1):
                ptrs[i + 1].next = ptrs[i]
            ps = [ptrs[0].next]
            for i in range(k - 1):
                if ps[i] and ps[i].next:
                    ps.append(ps[i].next)
                else:
                    break
            if len(ps) == k:
                ptrs[0].next = ps[-1]
            ptrs = ps

        return root

