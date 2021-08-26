"""
Solution of the easy problem - "Balanced Binary Tree",
https://leetcode.com/problems/balanced-binary-tree/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Is Balanced.

        >>> Solution().isBalanced(TreeNode(
        ...     3,
        ...     TreeNode(9),
        ...     TreeNode(20, TreeNode(15), TreeNode(7)),
        ... ))
        True
        >>> Solution().isBalanced(TreeNode(
        ...     1,
        ...     TreeNode(
        ...         2,
        ...         TreeNode(
        ...             3,
        ...             TreeNode(4),
        ...             TreeNode(4),
        ...         ),
        ...         TreeNode(3),
        ...     ),
        ...     TreeNode(2),
        ... ))
        False
        >>> Solution().isBalanced(TreeNode(
        ...     1,
        ...     TreeNode(2, TreeNode(3, TreeNode(4))),
        ...     TreeNode(2, None, TreeNode(3, None, TreeNode(4))),
        ... ))
        False

        """
        if not root:
            return True

        lheight = self.maxDepth(root.left)
        rheight = self.maxDepth(root.right)

        return (
            abs(rheight - lheight) <= 1 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        queue = [(1, root)] if root else []

        while queue:
            depth, node = queue.pop()
            maxdepth = max(depth, maxdepth)
            if node.left:
                queue.insert(0, (depth + 1, node.left))
            if node.right:
                queue.insert(0, (depth + 1, node.right))

        return maxdepth

