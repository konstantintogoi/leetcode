"""
Solution of the medium problem - "Combination Sum",
https://leetcode.com/problems/combination-sum/
"""
from typing import List, Set, Tuple


class Solution:
    def combinationSum(
        self,
        candidates: List[int],
        target: int,
        memo = None,
    ) -> Set[Tuple[int]]:
        """Combination Sum.

        >>> Solution().combinationSum([2, 3, 6, 7], 7)
        {(2, 2, 3), (7,)}
        >>> Solution().combinationSum([2, 3, 5], 8)
        {(2, 2, 2, 2), (2, 3, 3), (3, 5)}
        >>> Solution().combinationSum([2], 1)
        {}

        """
        if target == 0:
            return {}

        if memo is None:
            memo = {}
            candidates = sorted(candidates)

        if target in memo:
            return memo[target]

        if target < candidates[0]:
            return {}

        combs = set()

        for candidate in candidates:
            if candidate > target:
                break
            elif candidate < target:
                subtarget = target - candidate
                subcombs = self.combinationSum(candidates, subtarget, memo)
                for comb in subcombs:
                    combs.add(tuple(sorted((candidate, *comb))))
            else:
                combs.add((target, ))

        memo[target] = combs

        return memo[target]

