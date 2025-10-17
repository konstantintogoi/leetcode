"""
Solution of the medium problem
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"Binary Tree Zigzag Level Order Traversal"
"""
from heapq import heappop, heappush
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Return the zigzag level order traversal of nodes values.

        >>> Solution().zigzagLevelOrder(
        ...     TreeNode(3,
        ...         TreeNode(9),
        ...         TreeNode(20, TreeNode(15), TreeNode(7))
        ...     )
        ... )
        [[3], [20, 9], [15, 7]]
        >>> Solution().zigzagLevelOrder(TreeNode(1))
        [[1]]
        >>> Solution().zigzagLevelOrder(None)
        []

        """
        curlevel = 1
        childrank = 1
        levelnodes = []
        reverse = False

        traversal = []
        queue = [(curlevel, 1, root)] if root else []

        while queue:
            level, rank, node = heappop(queue)

            if level > curlevel:
                curlevel = level
                traversal.append(
                    levelnodes
                    if not reverse else
                    levelnodes[::-1]
                )
                reverse = not reverse
                levelnodes = [node.val]
                childrank = 1
            else:
                levelnodes.append(node.val)

            if node.left:
                heappush(queue, (level + 1, childrank, node.left))
                childrank += 1
            if node.right:
                heappush(queue, (level + 1, childrank, node.right))
                childrank += 1

        if levelnodes:
            traversal.append(levelnodes if not reverse else levelnodes[::-1])

        return traversal

