"""
Solution of the medium problem - "Advantage Shuffle",
https://leetcode.com/problems/advantage-shuffle/
"""
from collections import deque
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """Advantage Shuffle.

        >>> Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11])
        [2, 11, 7, 15]
        >>> Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11])
        [24, 32, 8, 12]

        """
        a = deque(sorted(A))
        b = sorted(range(len(A)), key=B.__getitem__)
        c = [None] * len(A)

        for i in range(len(A) - 1, -1, -1):
            c[b[i]] = a.pop() if B[b[i]] < a[-1] else a.popleft()

        return c

