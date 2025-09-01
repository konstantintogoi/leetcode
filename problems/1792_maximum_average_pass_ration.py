"""
Solution of the medium problem
https://leetcode.com/problems/maximum-average-pass-ratio/
"Maximum Average Pass Ratio"
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """Return the maximum average pass ratio.

        >>> Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)
        0.78333
        >>> Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4)
        0.53485

        """
        ratiosum = 0
        ratiodiffs = []
        for classnum, (npass, ntotal) in enumerate(classes):
            diff = (npass + 1) / (ntotal + 1) - npass / ntotal
            heappush(ratiodiffs, (-diff, classnum))
            ratiosum += (npass / ntotal)

        for _ in range(extraStudents):
            diff, classnum = heappop(ratiodiffs)
            ratiosum -= diff

            classes[classnum][0] += 1
            classes[classnum][1] += 1

            npass, ntotal = classes[classnum]

            diff = (npass + 1) / (ntotal + 1) - npass / ntotal
            heappush(ratiodiffs, (-diff, classnum))

        return round(ratiosum / len(classes), 5)

