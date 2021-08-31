"""
Solution of the easy problem -
"Same Tree",
https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Same Tree.

        >>> Solution().isSameTree(
        ...     TreeNode(1, TreeNode(2), TreeNode(3)),
        ...     TreeNode(1, TreeNode(2), TreeNode(3)),
        ... )
        True
        >>> Solution().isSameTree(
        ...     TreeNode(1, TreeNode(2)),
        ...     TreeNode(1, None, TreeNode(2)),
        ... )
        False
        >>> Solution().isSameTree(
        ...     TreeNode(1, TreeNode(2), TreeNode(1)),
        ...     TreeNode(1, TreeNode(1), TreeNode(2)),
        ... )
        False

        """
        return self.bfs(p) == self.bfs(q)

    def bfs(self, root):
        heap, queue = [], [(root, 1)]

        while queue:
            node, level = queue.pop()
            heap.append(node.val if node else None)
            if node and (node.left or node.right):
                queue.insert(0, (node.left, level + 1))
                queue.insert(0, (node.right, level + 1))

        return heap

