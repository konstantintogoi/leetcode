"""
Solution of the easy problem - "Minimum Depth of Binary Tree",
https://leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Min Depth.

        >>> Solution().minDepth(TreeNode(
        ...     3,
        ...     TreeNode(9),
        ...     TreeNode(20, TreeNode(15), TreeNode(7)),
        ... ))
        2
        >>> Solution().minDepth(TreeNode(
        ...     2, None, TreeNode(
        ...         3, None, TreeNode(
        ...             4, None, TreeNode(
        ...                 5, None, TreeNode(
        ...                     6, None, None
        ...                 ),
        ...             ),
        ...         ),
        ...     ),
        ... ))
        5
        >>> Solution().minDepth(None)
        0

        """
        mindepth = float('inf')
        queue = [(root, 1)] if root else []

        while queue:
            node, depth = queue.pop()

            if node.left is None and node.right is None:
                mindepth = min(depth, mindepth)
            if node.left:
                queue.insert(0, (node.left, depth + 1))
            if node.right:
                queue.insert(0, (node.right, depth + 1))

        return mindepth if root else 0

