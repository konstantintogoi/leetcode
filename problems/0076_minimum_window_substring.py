"""
Solution of the hard problem
https://leetcode.com/problems/minimum-window-substring/
"Minimum Window Substring"
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the minimum window substring of `s`.

        >>> Solution().minWindow('ADOBECODEBANC', 'ABC')
        'BANC'
        >>> Solution().minWindow('a', 'a')
        'a'
        >>> Solution().minWindow('a', 'aa')
        ''
        >>> Solution().minWindow('ab', 'b')
        'b'
        >>> Solution().minWindow('abc', 'a')
        'a'
        >>> Solution().minWindow('a', 'b')
        ''

        """
        if len(s) < len(t):
            return ''

        i, j = 0, len(t)
        tcntr = Counter(t)
        scntr = Counter(s[i:j])
        imin, jmin = 0, 100001

        while i <= len(s) - len(t):
            while j < len(s) and (scntr & tcntr) < tcntr:
                scntr[s[j]] += 1
                j += 1

            if (scntr & tcntr) < tcntr:
                break

            while i <= len(s) - len(t) and (scntr & tcntr) == tcntr:
                if scntr.total() < jmin - imin: imin, jmin = i, j
                scntr[s[i]] -= 1
                i += 1

        return s[imin:jmin] if jmin != 100001 else ''

