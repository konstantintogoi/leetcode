"""
Solution of the medium problem - "Combination Sum II",
https://leetcode.com/problems/combination-sum-ii/
"""
from collections import Counter
from typing import List, Set, Tuple


class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int,
        memo = None,
    ) -> List[List[int]]:
        """Combination Sum II.

        >>> Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        {(1, 7), (1, 1, 6), (1, 2, 5), (2, 6)}
        >>> Solution().combinationSum2([2, 5, 2, 1, 2], 5)
        {(1, 2, 2), (5,)}
        >>> Solution().combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6)
        {(2, 4), (2, 2, 2), (1, 2, 3), (1, 1, 2, 2), (1, 1, 4)}
        >>> Solution().combinationSum2([3, 2, 1, 5, 3, 4, 2], 10)
        {(3, 3, 4), (2, 2, 3, 3), (2, 3, 5), (1, 2, 3, 4), (1, 2, 2, 5), (1, 4, 5)}

        """
        if target == 0:
            return {}

        if not candidates:
            return {}

        if memo is None:
            memo = {}
            candidates = tuple(sorted(candidates))

        if (target, candidates) in memo:
            return memo[target, candidates]

        if target < candidates[0]:
            return {}

        combs = set()

        for i, candidate in enumerate(candidates):
            if candidate > target:
                break
            elif candidate < target:
                subtarget = target - candidate
                subcandidates = candidates[:i] + candidates[i + 1:]
                subcombs = self.combinationSum2(subcandidates, subtarget, memo)
                for subcomb in subcombs:
                    comb = tuple(sorted((candidate, *subcomb)))
                    combcounter = Counter(comb)
                    candcounter = Counter(candidates)
                    if all(candcounter[c] >= combcounter[c] for c in comb):
                        combs.add(comb)
            else:
                combs.add((target, ))

        memo[target, candidates] = combs

        return memo[target, candidates]

