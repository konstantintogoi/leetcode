"""
Solution of the easy problem - "Maximum Depth of Binary Tree",
https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Maximum Depth.

        >>> Solution().maxDepth(TreeNode(
        ...     3,
        ...     TreeNode(4),
        ...     TreeNode(20, TreeNode(15), TreeNode(7)),
        ... ))
        3
        >>> Solution().maxDepth(TreeNode(1, None, TreeNode(2)))
        2

        """
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

