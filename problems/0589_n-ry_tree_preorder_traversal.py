"""
Solution of the easy problem
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"N-ary Tree Preorder Traversal"
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List['Node']] = None,
    ):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """Return the preorder traversal of an n-ary tree.

        >>> Solution().preorder(
        ...     Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        ... )
        [1, 3, 5, 6, 2, 4]
        >>> Solution().preorder(
        ...     Node(1, [
        ...         Node(2),
        ...         Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        ...         Node(4, [Node(8, [Node(12)])]),
        ...         Node(5, [Node(9, [Node(13)]), Node(10)]),
        ...     ])
        ... )
        [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

        """
        if not root:
            return []

        res=[]
        queue = deque([root])

        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.children:
                for i in range(len(node.children) - 1, -1, -1):
                    queue.appendleft(node.children[i])

        return res

