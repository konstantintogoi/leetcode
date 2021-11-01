"""
Solution of the easy problem
https://leetcode.com/problems/binary-tree-inorder-traversal/
"Binary Tree Inorder Traversal"
"""
from typing import List


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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """Inorder Traversal.

        >>> Solution().inorderTraversal(
        ...     TreeNode(1, None, TreeNode(2, TreeNode(3)))
        ... )
        [1, 3, 2]
        >>> Solution().inorderTraversal(TreeNode(None))
        []
        >>> Solution().inorderTraversal(TreeNode(1))
        [1]
        >>> Solution().inorderTraversal(TreeNode(1, TreeNode(2)))
        [2, 1]
        >>> Solution().inorderTraversal(TreeNode(1, None, TreeNode(2)))
        [1, 2]

        """
        table = []
        if root is None or root.val is None:
            return table
        self.bfs(root, table)
        return table

    def bfs(self, node: TreeNode, table: List[TreeNode]):
        if not node: return table

        self.bfs(node.left, table)
        table.append(node.val)
        self.bfs(node.right, table)

        return table
