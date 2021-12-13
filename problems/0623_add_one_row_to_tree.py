"""
Solution of the medium problem
https://leetcode.com/problems/add-one-row-to-tree/
"Add One Row to Tree"
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
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """Add One Row.

        >>> root = TreeNode(
        ...     4,
        ...     TreeNode(2, TreeNode(3), TreeNode(1)),
        ...     TreeNode(6, TreeNode(5)),
        ... )
        >>> Solution().addOneRow(root, 1, 2)
        [4, 1, 1, 2, None, None, 6, 3, 1, 5]
        >>> 
        >>> root = TreeNode(
        ...     4,
        ...     TreeNode(2, TreeNode(3), TreeNode(1)),
        ...     TreeNode(6, TreeNode(5)),
        ... )
        >>> Solution().addOneRow(root, 1, 3)
        [4, 2, 6, 1, 1, 1, 1, 3, None, None, 1, 5]
        >>> 
        >>> root = TreeNode(
        ...     4,
        ...     TreeNode(2, TreeNode(3), TreeNode(1)),
        ...     TreeNode(6, TreeNode(5)),
        ... )
        >>> Solution().addOneRow(root, 1, 1)
        [1, 4, None, 2, 6, 3, 1, 5]
        >>> 
        >>> root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
        >>> Solution().addOneRow(root, 1, 3)
        [4, 2, None, 1, 1, 3, None, None, 1]

        """
        if d == 1: return TreeNode(v, root)
        level, queue = 1, [(root, 1)]

        while queue:
            node, level = queue.pop()
            if level == d - 1:
                node.left = TreeNode(v, left=node.left)
                node.right = TreeNode(v, right=node.right)
            if node.left:
                queue.insert(0, (node.left, level + 1))
            if node.right:
                queue.insert(0, (node.right, level + 1))

        return root
