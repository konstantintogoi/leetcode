"""
Solution of the medium problem
https://leetcode.com/problems/construct-binary-tree-from-string/
"Construct Binary Tree from String"
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
    def str2tree(self, s: str) -> TreeNode:
        """String to Tree.

        >>> Solution().str2tree('2')
        [2]
        >>> Solution().str2tree('2(3)(1)')
        [2, 3, 1]
        >>> Solution().str2tree('4(2(3)(1))')
        [4, 2, 3, 1]
        >>> Solution().str2tree('4(2(3)(1))(6(5))')
        [4, 2, 6, 3, 1, 5]
        >>> Solution().str2tree('4(2(3)(1))(6(5)(7))')
        [4, 2, 6, 3, 1, 5, 7]
        >>> Solution().str2tree('-4(2(3)(1))(6(5)(7))')
        [-4, 2, 6, 3, 1, 5, 7]
        >>> Solution().str2tree('51(232)(434)')
        [51, 232, 434]

        """
        it = iter(s) if isinstance(s, str) else s

        val = next(it, None)
        if val is None or val == ')':
            return
        elif val == '(':
            val = next(it)
        if val == '-':
            val += next(it)

        par = next(it, None)
        while par not in {None, '(', ')'}:
            val += par
            par = next(it, None)
        head = TreeNode(int(val))

        if par == '' or par == ')':
            return head
        left = self.str2tree(it)
        if left is None:
            return head
        head.left = left

        par = next(it, None)
        if par is None or par == ')':
            return head
        right = self.str2tree(it)
        if right is None:
            return head
        head.right = right

        next(it, None)  # close second bracket

        return head
