"""
Solution of the easy problem
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"Convert Sorted Array to Binary Search Tree"
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Sorted array to BST.

        >>> Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        [0, -3, 9, -10, None, 5]
        >>> Solution().sortedArrayToBST([1, 3])
        [3, 1]

        """
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))
        elif len(nums) == 3:
            return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))

        n = len(nums)
        midval = nums[n // 2]
        left = self.sortedArrayToBST(nums[:n // 2])
        right = self.sortedArrayToBST(nums[n // 2 + 1:])

        return TreeNode(midval, left, right)
