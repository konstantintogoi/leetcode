"""
Solution of the medium problem
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"Construct Binary Tree from Preorder and Inorder Traversal"
"""
from typing import List, Optional


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
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:
        """Construct and return the binary tree.

        >>> Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        [3, 9, 20, None, None, 15, 7]
        >>> Solution().buildTree([-1], [-1])
        [-1]

        """
        ixs = {val: i for i, val in enumerate(inorder)}
        ix = 0

        def buildSubTree(lo, hi) -> Optional[TreeNode]:
            if lo >= hi:
                return None

            nonlocal ix
            rootval = preorder[ix]
            root = TreeNode(rootval)
            ix += 1

            mid = ixs[rootval]
            root.left = buildSubTree(lo, mid)
            root.right = buildSubTree(mid + 1, hi)
            return root

        return buildSubTree(0, len(inorder))

