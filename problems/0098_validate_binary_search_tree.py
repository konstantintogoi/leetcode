"""
Solution of the medium problem
https://leetcode.com/problems/validate-binary-search-tree/
"Validate Binary Search Tree"
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Return `True` if `root` is a valid binary search tree (BST).

        >>> Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
        True
        >>> Solution().isValidBST(
        ...     TreeNode(5,
        ...         TreeNode(1),
        ...         TreeNode(4, TreeNode(3), TreeNode(6))
        ...     )
        ... )
        False
        >>> Solution().isValidBST(
        ...     TreeNode(5,
        ...         TreeNode(4),
        ...         TreeNode(6, TreeNode(3), TreeNode(7))
        ...     )
        ... )
        False
        >>> Solution().isValidBST(TreeNode(0, None, TreeNode(1)))
        True
        >>> Solution().isValidBST(
        ...     TreeNode(3,
        ...         TreeNode(1, TreeNode(0), TreeNode(2)),
        ...         TreeNode(5, TreeNode(4), TreeNode(6)),
        ...     )
        ... )
        True

        """
        def isvalidnode(node: TreeNode, lo: int, hi: int) -> bool:
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False

            if node.left and node.left.val <= lo:
                return False
            if node.right and node.right.val >= hi:
                return False

            if node.left and not isvalidnode(node.left, lo, node.val):
                return False
            if node.right and not isvalidnode(node.right, node.val, hi):
                return False

            return True

        return isvalidnode(root, float('-inf'), float('inf'))

