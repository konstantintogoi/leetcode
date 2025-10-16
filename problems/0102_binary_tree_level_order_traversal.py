"""
Solution of the medium problem
https://leetcode.com/problems/binary-tree-level-order-traversal/
"Binary Tree Level Order Traversal"
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Return the level order traversal of the nodes values.

        >>> Solution().levelOrder(
        ...     TreeNode(3,
        ...         TreeNode(9),
        ...         TreeNode(20, TreeNode(15), TreeNode(7))
        ...     )
        ... )
        [[3], [9, 20], [15, 7]]
        >>> Solution().levelOrder(TreeNode(1))
        [[1]]
        >>> Solution().levelOrder(None)
        []

        """
        traversed = []

        currlevel = 0
        queue = deque([(root, currlevel)] if root else [])
        levelnodes = []

        while queue:
            node, level = queue.pop()
            if level != currlevel:
                traversed.append(levelnodes)
                currlevel = level
                levelnodes = []

            levelnodes.append(node.val)

            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))

        if levelnodes:
            traversed.append(levelnodes)

        return traversed

