"""
Solution of the meduim problem - "Beautiful Arrangement II",
https://leetcode.com/problems/beautiful-arrangement-ii/
"""
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """Construct Array.

        >>> Solution().constructArray(3, 1)
        [1, 2, 3]
        >>> Solution().constructArray(3, 2)
        [1, 3, 2]

        """
        ans = [0] * n
        l, r = 1, k + 1

        for i in range(k + 1):
            if i % 2:
                ans[i] = r
                r -= 1
            else:
                ans[i] = l
                l += 1

        for i in range(k + 1,n):
            ans[i] = i + 1

        return ans

