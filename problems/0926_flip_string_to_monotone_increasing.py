"""
Solution of the medium problem
https://leetcode.com/problems/flip-string-to-monotone-increasing/
"Flip String to Monotone Increasing"
"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """Return the minimum number of flips to make `s` monotone increasing.

        >>> Solution().minFlipsMonoIncr('00110')
        1
        >>> Solution().minFlipsMonoIncr('010110')
        2
        >>> Solution().minFlipsMonoIncr('00011000')
        2

        """
        ones, ans = 0, 0

        for num in s:
            if num == '1':
                ones += 1
            elif ones:
                ones -= 1
                ans += 1

        return ans

