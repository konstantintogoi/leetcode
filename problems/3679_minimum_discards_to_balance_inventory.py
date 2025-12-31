"""
Solution of the medium problem
https://leetcode.com/problems/minimum-discards-to-balance-inventory/
"Minimum Discards to Balance Inventory"
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minArrivalsToDiscard(
        self,
        arrivals: List[int],
        w: int,
        m: int,
    ) -> int:
        """Return the minimum number of arrivals to be discarded
        so that every `w`-day window contains at most `m` occurences.

        >>> Solution().minArrivalsToDiscard([1, 2, 1, 3, 1], 4, 2)
        0
        >>> Solution().minArrivalsToDiscard([1, 2, 3, 3, 3, 4], 3, 2)
        1
        >>> Solution().minArrivalsToDiscard([10,4,3,6,4,5,6,1,4], 7, 1)
        2

        """
        discarded = defaultdict(bool)
        kept = defaultdict(int)
        ndiscarded = 0
        h = []

        for i, arrival in enumerate(arrivals):
            if len(h) == w:
                j, a = heappop(h)
                if not discarded[j]:
                    kept[a] -= 1

            heappush(h, (i + 1, arrival))

            if kept[arrival] == m:
                discarded[i + 1] = True
                ndiscarded += 1
            else:
                kept[arrival] += 1

        return ndiscarded

