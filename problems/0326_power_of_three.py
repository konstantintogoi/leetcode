"""
Solution of the easy problem - "Power of Three",
https://leetcode.com/problems/power-of-three/
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """Is Power of Three.

        >>> Solution().isPowerOfThree(27)
        True
        >>> Solution().isPowerOfThree(0)
        False
        >>> Solution().isPowerOfThree(9)
        True
        >>> Solution().isPowerOfThree(45)
        False

        """
        i = 1
        while True:
            if i == n: return True
            i *= 3
            if i > n: break
        return False

