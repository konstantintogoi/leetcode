"""
Solution of the medium problem
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"Successful Pairs of Spells and Potions"
"""
from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(
        self,
        spells: List[int],
        potions: List[int],
        success: int,
    ) -> List[int]:
        """Return an integer array `pairs` of length `n`.

        >>> Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
        [4, 0, 3]


        """
        potions.sort()
        n = len(spells)
        m = len(potions)

        ans = []
        for spellstrength in spells:
            strength = success / spellstrength
            ans.append(m - bisect_left(potions, strength))
        return ans

