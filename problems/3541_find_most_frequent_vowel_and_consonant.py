"""
Solution of the easy problem
https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
"Find Most Frequent Vowel and Consonant"
"""
from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        """Return the sum of the two frequencies.

        >>> Solution().maxFreqSum('successes')
        6
        >>> Solution().maxFreqSum('aeiaeia')
        3

        """
        cnts = defaultdict(int)
        for c in s: cnts[c] += 1

        maxvowcnt = 0
        maxconscnt = 0

        for c, cnt in cnts.items():
            if c in {'a', 'e', 'i', 'o', 'u'}:
                maxvowcnt = max(cnt, maxvowcnt)
            else:
                maxconscnt = max(cnt, maxconscnt)

        return maxvowcnt + maxconscnt

