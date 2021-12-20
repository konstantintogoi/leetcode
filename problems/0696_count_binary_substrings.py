"""
Solution of the easy problem
https://leetcode.com/problems/count-binary-substrings/
"Count Binary Substrings"
"""
from itertools import groupby


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """Count Binary Substrings.

        >>> Solution().countBinarySubstrings('00110011')
        6
        >>> Solution().countBinarySubstrings('10101')
        4
        >>> Solution().countBinarySubstrings('00110')
        3

        """
        cnt = 0
        subs = ''
        for k, g in groupby(s):
            ss = ''.join(list(g))
            cnt += min(len(ss), len(subs))
            subs = ss
        return cnt
