"""
Solution of "Trim a Binary Search Tree" problem at
https://leetcode.com/problems/trim-a-binary-search-tree/
"""
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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """Trim a BST.

        >>> tree = TreeNode(1, TreeNode(0), TreeNode(2))
        >>> Solution().trimBST(tree, 1, 2)
        [1, None, 2]
        >>> tree = TreeNode(
        ...     3,
        ...     TreeNode(0, None, TreeNode(2, TreeNode(1))),
        ...     TreeNode(4),
        ... )
        >>> Solution().trimBST(tree, 1, 3)
        [3, 2, None, 1]
        >>> tree = TreeNode(1)
        >>> Solution().trimBST(tree, 1, 2)
        [1]
        >>> tree = TreeNode(1, None, TreeNode(2))
        >>> Solution().trimBST(tree, 1, 3)
        [1, None, 2]
        >>> tree = TreeNode(1, None, TreeNode(2))
        >>> Solution().trimBST(tree, 2, 4)
        [2]
        >>> tree = TreeNode(1, None, TreeNode(2))
        >>> Solution().trimBST(tree, 3, 4)
        >>> tree = TreeNode(
        ...     3,
        ...     TreeNode(1, None, TreeNode(2)),
        ...     TreeNode(4),
        ... )
        >>> Solution().trimBST(tree, 3, 4)
        [3, None, 4]

        """
        if root and root.left:
            root.left = self.trimBST(root.left, low, high)
        if root and root.right:
            root.right = self.trimBST(root.right, low, high)

        while root and root.val < low:
            root = root.right
        while root and root.val > high:
            root = root.left

        return root
