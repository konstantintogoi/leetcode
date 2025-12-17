"""
Solution of the easy problem
https://leetcode.com/problems/find-the-pivot-integer/
"Find the Pivot Integer
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        """Return the pivot integer `x`. If no such integer exists, return -1.

        >>> Solution().pivotInteger(8)
        6
        >>> Solution().pivotInteger(1)
        1
        >>> Solution().pivotInteger(4)
        -1

        """
        cumsums = [1]
        invcumsums = [n]

        for i in range(2, n + 1):
            cumsums.append(cumsums[-1] + i)

        for i in range(n - 1, 0, -1):
            invcumsums.append(invcumsums[-1] + i)

        for i, cumsum in enumerate(cumsums):
            if cumsums[i] == invcumsums[n - 1 - i]:
                return i + 1

        return -1

