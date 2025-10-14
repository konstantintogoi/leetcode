"""
Solution of the medium problem
https://leetcode.com/problems/recover-binary-search-tree/
"Recover Binary Search Tree"
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """Recover the tree without changing its structure.

        >>> tree = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
        >>> Solution().recoverTree(tree)
        >>> tree
        [3, 1, None, None, 2]
        >>> tree = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
        >>> Solution().recoverTree(tree)
        >>> tree
        [2, 1, 4, None, None, 3]

        """
        node = root
        prev = None

        first = None
        last = None

        def checknswap():
            nonlocal prev, node, first, last
            if prev and prev.val > node.val:
                if not first:
                    first, last = prev, node
                else:
                    last = node

        while node:
            if not node.left:
                checknswap()
                prev = node
                node = node.right
            else:
                right = node.left
                while right.right and right.right != node:
                    right = right.right

                if not right.right:
                    right.right = node
                    node = node.left
                else:
                    right.right = None

                    checknswap()
                    prev = node
                    node = node.right

        first.val, last.val = last.val, first.val

