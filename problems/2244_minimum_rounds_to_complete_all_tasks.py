"""
Solution of the medium problem
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
"Minimum Rounds to Complete All Tasks"
"""
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """Return the minimum rounds required to complete all the tasks.

        >>> Solution().minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
        4
        >>> Solution().minimumRounds([2, 3, 3])
        -1

        """
        tasks.sort()
        tasks.append(0)
        cnt = 0

        t, n = 0, 0
        for i in range(len(tasks)):
            if tasks[i] == t:
                n += 1
            elif n % 3 == 0:
                cnt += n / 3
                t = tasks[i]
                n = 1
            elif n % 3 == 2:
                cnt += (n // 3 + 1)
                t = tasks[i]
                n = 1
            elif n > 3:
                cnt += (n // 3 + 1)
                t = tasks[i]
                n = 1
            else:
                cnt = -1
                break

        return int(cnt)

