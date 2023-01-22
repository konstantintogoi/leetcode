"""
Solution of the easy problem
https://leetcode.com/problems/find-the-town-judge/
"Find the Town Judge"
"""
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """Return the label of the town judge.

        >>> Solution().findJudge(2, [[1, 2]])
        2
        >>> Solution().findJudge(3, [[1, 3], [2, 3]])
        3
        >>> Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]])
        -1
        >>> Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
        3
        >>> Solution().findJudge(4, [[1, 3], [1, 4], [2, 3]])
        -1

        """
        fwd_edges = defaultdict(list)
        bck_edges = defaultdict(list)

        for a, b in trust:
            fwd_edges[a].append(b)
            bck_edges[b].append(a)

        judge = set(range(1, n + 1))
        for a in fwd_edges:
            judge = judge.intersection(set(fwd_edges[a]))

        if len(judge) != 1:
            return -1
        judge = list(judge)[0]
        if len(bck_edges[judge]) != n - 1:
            return -1
        return judge

