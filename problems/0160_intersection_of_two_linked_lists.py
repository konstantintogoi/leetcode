"""
Solution of "Intersection of Two Linked Lists" problem at
https://leetcode.com/problems/intersection-of-two-linked-lists/
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """Get intersection.

        >>> c = ListNode(8, ListNode(4, ListNode(5)))
        >>> b = ListNode(5, ListNode(6, ListNode(1, c)))
        >>> a = ListNode(4, ListNode(1, c))
        >>> Solution().getIntersectionNode(a, b)
        [8, 4, 5]
        >>> c = ListNode(2, ListNode(4))
        >>> b = ListNode(3, c)
        >>> a = ListNode(1, ListNode(9, ListNode(1, c)))
        >>> Solution().getIntersectionNode(a, b)
        [2, 4]
        >>> c = None
        >>> b = ListNode(1, ListNode(5, c))
        >>> a = ListNode(2, ListNode(6, ListNode(4, c)))
        >>> Solution().getIntersectionNode(a, b)

        """
        if not headA or not headB: return
        if id(headA) == id(headB): return headA

        diff = 0

        node = headA
        while node:
            diff += 1
            node = node.next
        node = headB
        while node:
            diff -= 1
            node = node.next

        for i in range( diff): headA = headA.next
        for i in range(-diff): headB = headB.next

        while id(headA) != id(headB):
            headA = headA.next
            headB = headB.next
        return headA

