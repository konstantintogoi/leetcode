"""
Solution of the easy problem
https://leetcode.com/problems/cousins-in-binary-tree/
"Cousins in Binary Tree"
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
            # else: vals.append(None)

            if node: queue.insert(0, node.left)
            if node: queue.insert(0, node.right)

        while vals[-1] is None: vals.pop()

        return repr(vals)


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """Cousins in Binary Tree.

        >>> Solution().isCousins(TreeNode(
        ...     1, TreeNode(2, TreeNode(4)), TreeNode(3)
        ... ), 3, 4)
        False
        >>> Solution().isCousins(TreeNode(
        ...     1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5))
        ... ), 5, 4)
        True
        >>> Solution().isCousins(TreeNode(
        ...     1, TreeNode(2, None, TreeNode(4)), TreeNode(3)
        ... ), 2, 3)
        False

        """
        x_depth, x_parent_value = self.bfs(x, root)
        y_depth, y_parent_value = self.bfs(y, root)
        return x_depth == y_depth and x_parent_value != y_parent_value

    def bfs(self, val, node=None, queue=None):
        queue = queue or [(node, 0, None)]
        node, depth, parent_value = queue.pop()

        if node.val == val:
            return depth, parent_value
        if node.left:
            queue.insert(0, (node.left, depth + 1, node.val))
        if node.right:
            queue.insert(0, (node.right, depth + 1, node.val))
        if queue:
            return self.bfs(val, queue=queue)

        return -1, None
