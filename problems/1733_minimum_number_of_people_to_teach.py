"""
Solution of the medium problem
https://leetcode.com/problems/minimum-number-of-people-to-teach/
"Minimum Number of People to Teach"
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTeachings(
        self,
        n: int,
        languages: List[List[int]],
        friendships: List[List[int]],
    ) -> int:
        """Return the minimum number of users you need to teach.

        >>> Solution().minimumTeachings(
        ... 2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]
        ... )
        1
        >>> Solution().minimumTeachings(
        ... 3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]]
        ... )
        2
        >>> Solution().minimumTeachings(
        ...     2,
        ...     [
        ...         [2], [1], [2,1], [1], [1,2], [1], [2], [1], [1],
        ...         [2], [1,2], [1,2], [1,2], [2,1], [1], [2], [1,2]
        ...     ],
        ...     [
        ...         [15,16], [4,13], [3,16], [5,14], [1,7], [2,11],
        ...         [3,15], [4,16], [7,9], [6,13], [6,16], [4,10],
        ...         [6,9], [5,6], [7,12], [6,12], [3,7], [4,7], [8,10]
        ...     ]
        ... )
        3

        """
        languages = [set(langs) for langs in languages]
        needteaching = set()

        for x, y in friendships:
            if languages[x - 1].intersection(languages[y - 1]):
                continue
            needteaching.add(x)
            needteaching.add(y)

        ans = float('inf')

        for lang in range(1, n + 1):
            cnt = sum(1 for x in needteaching if lang not in languages[x - 1])
            ans = min(ans, cnt)

        return ans

