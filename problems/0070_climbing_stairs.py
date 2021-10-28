"""
Solution of the easy problem
https://leetcode.com/problems/climbing-stairs/
"Climbing Stairs"
"""
class Solution:
    def climbingStairs(self, n: int) -> int:
        """Climbing Stairs.

        >>> Solution().climbingStairs(1)
        1
        >>> Solution().climbingStairs(2)
        2
        >>> Solution().climbingStairs(3)
        3
        >>> Solution().climbingStairs(4)
        5
        >>> Solution().climbingStairs(5)
        8

        """
        if n < 4: return n
        table = [1, 2, 3]
        for i in range(3, n):
            table.append(table[i - 2] + table[i - 1])
        return table[n - 1]
