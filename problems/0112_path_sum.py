"""
Solution of the easy problem
https://leetcode.com/problems/path-sum/
"Path Sum"
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Has Path Sum.

        >>> Solution().hasPathSum(TreeNode(
        ...     5,
        ...     TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        ...     TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        ... ), 22)
        True
        >>> Solution().hasPathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5)
        False
        >>> Solution().hasPathSum(None, 0)
        False

        """
        pathsums = set()
        queue = [root] if root else []

        while queue:
            node = queue.pop()

            if node.left is None and node.right is None:
                pathsums.add(node.val)
            if node.left:
                node.left.val += node.val
                queue.insert(0, node.left)
            if node.right:
                node.right.val += node.val
                queue.insert(0, node.right)

        return targetSum in pathsums
