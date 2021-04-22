"""
Solution of the easy problem - "First Bad Version",
https://leetcode.com/problems/first-bad-version/
"""
class Solution:
    def firstBadVersion(self, n, bad=None):
        """First Bad Version.

        >>> Solution().firstBadVersion(5, 4)
        4
        >>> Solution().firstBadVersion(1, 1)
        1

        """
        def isBadVersion(i):
            """For doctests."""
            return i >= bad

        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid

        return r

