"""
Solution of the easy problem
https://leetcode.com/problems/largest-unique-number/
"Largest Unique Number"
"""
from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        """Return the largest integer in the array that appears exactly once.

        >>> Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1])
        8
        >>> Solution().largestUniqueNumber([9, 9, 8, 8])
        -1

        """
        seen = {}
        for a in A: seen[a] = seen.get(a, 0) + 1
        seen = [a for a in seen if seen[a] == 1]
        return max(seen) if seen else -1

