"""
Solution of the easy problem
https://leetcode.com/problems/binary-tree-preorder-traversal/
"Binary Tree Preorder Traversal"
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Return the preorder traversal of its nodes' values.

        >>> Solution().preorderTraversal(
        ...     TreeNode(1, None, TreeNode(2, TreeNode(3))),
        ... )
        [1, 2, 3]
        >>> Solution().preorderTraversal(None)
        []
        >>> Solution().preorderTraversal(TreeNode(1))
        [1]

        """
        table = []

        def bfs(node):
            if node:
                table.append(node.val)
                bfs(node.left)
                bfs(node.right)

        bfs(root)
        return table

