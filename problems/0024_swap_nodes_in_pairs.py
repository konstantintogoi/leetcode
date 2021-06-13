"""
Solution of the medium problem - "Swap Nodes in Pairs",
https://leetcode.com/problems/swap-nodes-in-pairs/
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
    def swapPairs(self, head: ListNode) -> ListNode:
        """Swap Nodes in Pairs.

        >>> Solution().swapPairs(
        ...     ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        ... )
        [2, 1, 4, 3]
        >>> Solution().swapPairs(ListNode(1))
        [1]

        """
        root = fst = head

        while fst and fst.next:
            snd = fst.next
            fst.val, snd.val = snd.val, fst.val
            fst = snd.next
            snd = fst.next if fst else None

        return root

