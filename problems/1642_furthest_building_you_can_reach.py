"""
Solution of the medium problem - "Furthest Building You Can Reach",
https://leetcode.com/problems/furthest-building-you-can-reach/
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def furthestBuilding(
        self,
        heights: List[int],
        bricks: int,
        ladders: int,
    ) -> int:
        """Furthest Building.

        >>> Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1)
        4
        >>> Solution().furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2)
        7
        >>> Solution().furthestBuilding([14, 3, 19, 3], 17, 0)
        3

        """
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0: continue

            if ladders > 0:
                heappush(heap, diff)
                ladders -= 1
            elif heap and diff > heap[0]:
                heappush(heap, diff)
                bricks -= heappop(heap)
            else:
                bricks -= diff

            if bricks < 0:
                return i

        return len(heights) - 1

