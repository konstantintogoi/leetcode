"""
Solution of the medium problem - "Deepest Leaves Sum",
https://leetcode.com/problems/deepest-leaves-sum/
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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """Deepest Leaves Sum.

        >>> TN = TreeNode
        >>> 
        >>> Solution().deepestLeavesSum(TN(
        ...     1,
        ...     TN(2, TN(4, TN(7)), TN(5)),
        ...     TN(3, None, TN(6, None, TN(8))),
        ... ))
        15
        >>> 
        >>> Solution().deepestLeavesSum(TN(
        ...     6,
        ...     TN(7, TN(2, TN(9)), TN(7, TN(1), TN(4))),
        ...     TN(8, TN(1), TN(3, None, TN(5))),
        ... ))
        19

        """
        sums = []

        queue = [(root, 0)]

        while queue:
            node, level = queue.pop()

            if len(sums) <= level:
                sums.append(node.val)
            else:
                sums[level] += node.val

            if node.left:
                queue.insert(0, (node.left, level + 1))
            if node.right:
                queue.insert(0, (node.right, level + 1))

        return sums[-1]

