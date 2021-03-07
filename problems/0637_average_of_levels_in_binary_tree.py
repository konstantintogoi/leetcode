"""
Solution of "Average Levels in Binary Tree" problem at
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

