"""
Solution of the medium problem
https://leetcode.com/problems/unique-binary-search-trees-ii/
"Unique Binary Search Trees II"
"""
from typing import List, Optional


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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """Given an integer `n`, return all the structurally unique BST's.

        >>> Solution().generateTrees(3)
        [[1, None, 2, None, 3], [1, None, 3, 2], [2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]]
        >>> Solution().generateTrees(1)
        [[1]]

        """
        perms = []

        def perm(p):
            if len(p) == n:
                perms.append(p.copy())
                return

            for i in range(1, n + 1):
                if i not in p:
                    p.append(i)
                    perm(p)
                    p.pop()

        def bfs(tree):
            if tree.val is None:
                return []

            vals, queue = [], [tree]

            while queue:
                node = queue.pop()
                if node: vals.append(node.val)
                # else: vals.append(None)

                if node: queue.insert(0, node.left)
                if node: queue.insert(0, node.right)

            while vals[-1] is None:
                vals.pop()

            return tuple(vals)

        perm([])

        def treeinsert(tree, val):
            if val < tree.val and tree.left:
                treeinsert(tree.left, val)
            elif val < tree.val:
                tree.left = TreeNode(val)
            elif val > tree.val and tree.right:
                treeinsert(tree.right, val)
            else:
                tree.right = TreeNode(val)

        trees = []
        traversedtrees = set()

        for p in perms:
            tree = TreeNode(p[0])
            for i in range(1, len(p)):
                treeinsert(tree, p[i])

            treetraversal = bfs(tree)
            if treetraversal not in traversedtrees:
                traversedtrees.add(treetraversal)
                trees.append(tree)

        return trees

