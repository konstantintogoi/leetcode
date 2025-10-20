"""
Solution of the medium problem
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"Construct Binary Tree from Inorder and Postorder Traversal"
"""
from typing import Optional, List


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
        inorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:
        """Construct and return the binary tree.

        >>> Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        [3, 9, 20, None, None, 15, 7]
        >>> Solution().buildTree([-1], [-1])
        [-1]

        """
        def buildSubTree(ior, por) -> Optional[TreeNode]:
            if not ior:
                return None

            rootval = por.pop()
            rootix = ior.index(rootval)
            root = TreeNode(rootval)

            root.right = buildSubTree(ior[rootix + 1:], por)
            root.left = buildSubTree(ior[:rootix], por)

            return root

        return buildSubTree(inorder, postorder)

