"""
Solution of the medium problem - "Reconstruct Original Digits from English",
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        """Original Digits.

        >>> Solution().originalDigits('zerozero')
        '00'
        >>> Solution().originalDigits('owoztneoer')
        '012'
        >>> Solution().originalDigits('fviefuro')
        '45'

        """
        c = Counter(s)

        cs = {}
        cs['0'] = c['z']
        cs['2'] = c['w']
        cs['4'] = c['u']
        cs['6'] = c['x']
        cs['8'] = c['g']
        cs['3'] = c['h'] - cs['8']
        cs['5'] = c['f'] - cs['4']
        cs['7'] = c['s'] - cs['6']
        cs['9'] = c['i'] - cs['5'] - cs['6'] - cs['8']
        cs['1'] = c['n'] - cs['7'] - 2 * cs['9']

        return ''.join([key * cs[key] for key in sorted(cs.keys())])

