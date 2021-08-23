"""
Solution of the easy problem - "Symmetric Tree",
https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.val is None: return '[]'
        vals, queue = [], [self]

        while queue:
            node = queue.pop()
            if node: vals.append(node.val)
            else: vals.append(None)

            if node: queue.insert(0, node.left)
            if node: queue.insert(0, node.right)

        while vals[-1] is None: vals.pop()

        return repr(vals)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Is Symmetric.

        >>> Solution().isSymmetric(TreeNode(
        ...     1,
        ...     TreeNode(2, TreeNode(3), TreeNode(4)),
        ...     TreeNode(2, TreeNode(4), TreeNode(3)),
        ... ))
        True
        >>> Solution().isSymmetric(TreeNode(
        ...     1,
        ...     TreeNode(2, None, TreeNode(3)),
        ...     TreeNode(2, None, TreeNode(3)),
        ... ))
        False

        """
        def lbfs(head):
            if not head:
                return []
            vals = []
            queue = [head]

            while queue:
                node = queue.pop()
                if node:
                    vals.append(node.val)
                    queue.insert(0, node.left)
                    queue.insert(0, node.right)
                else:
                    vals.append(None)

            return vals

        def rbfs(head):
            if not head:
                return []
            vals = []
            queue = [head]

            while queue:
                node = queue.pop()
                if node:
                    vals.append(node.val)
                    queue.insert(0, node.right)
                    queue.insert(0, node.left)
                else:
                    vals.append(None)

            return vals

        return root and lbfs(root.left) == rbfs(root.right)

