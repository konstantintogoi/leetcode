"""
Solution of "Add Two Numbers"
problem at https://leetcode.com/problems/add-two-numbers/.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, node):
        this = self
        while this or node:
            node = node or ListNode()
            this = this or ListNode()

            if this.val != node.val:
                return False

            node = node.next
            this = this.next

        return True

    def __repr__(self):
        if self.val is None:
            return '[]'
        vals, node = [self.val], self.next
        while node:
            vals.append(node.val)
            node = node.next
        return repr(vals)



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Add two numbers.

        >>> Solution().addTwoNumbers(
        ... ListNode(2, next=ListNode(4, next=ListNode(3))),
        ... ListNode(5, next=ListNode(6, next=ListNode(4)))
        ... )
        [7, 0, 8]
        >>> 
        >>> Solution().addTwoNumbers(ListNode(5), ListNode(5))
        [0, 1]
        >>> 
        >>> Solution().addTwoNumbers(
        ...     ListNode(1),
        ...     ListNode(9, next=ListNode(9))
        ... )
        [0, 0, 1]

        """
        carry_flag = 0
        head = ListNode()
        prev_node = head

        while l1 or l2 or carry_flag:
            l1 = l1 or ListNode()
            l2 = l2 or ListNode()

            bitsum = (l1.val + l2.val + carry_flag) % 10
            carry_flag = (l1.val + l2.val + carry_flag) // 10

            node = ListNode(val=bitsum)
            prev_node.next = node
            prev_node = node

            l1 = l1.next
            l2 = l2.next

        return head.next

