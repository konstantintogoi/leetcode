"""
Solution of the easy problem
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"Average Levels in Binary Tree"
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """Average Of Levels.

        >>> Solution().averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(
        ...     20, TreeNode(15), TreeNode(7)
        ... )))
        [3.0, 14.5, 11.0]

        """
        queue = [(root, 0)]
        vals = {}

        while queue:
            node, level = queue.pop()
            if level in vals:
                vals[level].append(node.val)
            else:
                vals[level] = [node.val]

            if node.left:
                queue.insert(0, (node.left, level + 1))
            if node.right:
                queue.insert(0, (node.right, level + 1))

        return [sum(vs)/len(vs) for vs in vals.values()]
