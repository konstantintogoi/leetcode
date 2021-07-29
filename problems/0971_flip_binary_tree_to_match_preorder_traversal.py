"""
Solution of the medium problem -
"Flip Binary Tree To Match Preorder Traversal",
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
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
            # else: vals.append(None)

            if node: queue.insert(0, node.left)
            if node: queue.insert(0, node.right)

        while vals[-1] is None: vals.pop()

        return repr(vals)


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """Flip Binary Tree.

        >>> TN = TreeNode
        >>> 
        >>> Solution().flipMatchVoyage(TN(1, TN(2)), [2, 1])
        [-1]
        >>> Solution().flipMatchVoyage(TN(1, TN(2), TN(3)), [1, 3, 2])
        [1]
        >>> Solution().flipMatchVoyage(TN(1, TN(2), TN(3)), [1, 2, 3])
        []
        >>> Solution().flipMatchVoyage(TN(1, None, TN(2)), [1, 2])
        []
        >>> Solution().flipMatchVoyage(
        ...     TN(2, TN(1, TN(5)), TN(4, TN(3))),
        ...     [2, 4, 3, 1, 5],
        ... )
        [2]

        """
        n = len(voyage)
        flipped = []

        def dfs(node, i):
            if not node or node.val != voyage[i]:
                return i
            i += 1
            if node.left and i < n and voyage[i] == node.left.val:
                i = dfs(node.left, i)
                i = dfs(node.right, i)
            elif node.right and i < n and voyage[i] == node.right.val:
                if node.left:
                    flipped.append(node.val)
                i = dfs(node.right, i)
                i = dfs(node.left, i)
            return i

        return flipped if dfs(root, 0) == n else [-1]

