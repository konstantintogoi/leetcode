"""
Solution of the easy problem
https://leetcode.com/problems/palindrome-linked-list/
"Palindrome Linked List"
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
    def isPalindrome(self, head: ListNode) -> bool:
        """Is Palindrome.

        >>> N = ListNode
        >>> Solution().isPalindrome(N(1, N(2, N(2, N(1)))))
        True
        >>> Solution().isPalindrome(N(1, N(2)))
        False

        """
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        i, j = 0, len(vals) - 1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True
