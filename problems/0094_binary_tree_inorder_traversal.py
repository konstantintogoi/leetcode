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
        >>> Solution().inorderTraversal(TreeNode(1))
        [1]
        >>> Solution().inorderTraversal(TreeNode(1, TreeNode(2)))
        [2, 1]
        >>> Solution().inorderTraversal(TreeNode(1, None, TreeNode(2)))
        [1, 2]

        """
        traversal = []

        node = root
        while node:
            if not node.left:
                traversal.append(node.val)
                node = node.right
            else:
                prev = node.left
                while prev.right and prev.right != node:
                    prev = prev.right

                if not prev.right:
                    prev.right = node
                    node = node.left
                else:
                    prev.right = None
                    traversal.append(node.val)
                    node = node.right

        return traversal

