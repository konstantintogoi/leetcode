"""
Solution of the easy problem
https://leetcode.com/problems/find-closest-person/
"Find Closest Person"
"""
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """Find the closest person.

        >>> Solution().findClosest(2, 7, 4)
        1
        >>> Solution().findClosest(2, 5, 6)
        2
        >>> Solution().findClosest(1, 5, 3)
        0

        """
        if abs(z - x) < abs(z - y):
            return 1
        if abs(z - y) < abs(z - x):
            return 2
        return 0

