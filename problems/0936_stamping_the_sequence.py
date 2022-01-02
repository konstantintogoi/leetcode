"""
Solution of the hard problem
https://leetcode.com/problems/stamping-the-sequence/
"Stamping The Sequence"
"""
from collections import deque
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """Moves To Stamp.

        >>> Solution().movesToStamp('abc', 'ababc')
        [1, 0, 2]
        >>> Solution().movesToStamp('abca', 'aabcaca')
        [2, 3, 0, 1]

        """
        m, n = len(stamp), len(target)

        queue = deque()
        done = [False] * n
        ans = []
        A = []

        for i in range(n - m + 1):
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i + j]
                if a == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)

            A.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while queue:
            i = queue.popleft()

            for j in range(max(0, i - m + 1), min(n - m, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for k in A[j][0]:
                            if not done[k]:
                                queue.append(k)
                                done[k] = True

        return ans[::-1] if all(done) else []
