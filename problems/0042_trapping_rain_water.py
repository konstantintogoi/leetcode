"""
Solution of the hard problem - "Trapping Rain Water",
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Trap.

        >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6
        >>> Solution().trap([4, 2, 0, 3, 2, 5])
        9
        >>> Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
        23
        >>> Solution().trap([0])
        0
        >>> Solution().trap([
        ...     6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2,
        ...     7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3,
        ... ])
        83

        """
        height.insert(0, 0)
        height.append(0)

        peaks = []
        for i in range(1, len(height) - 1):
            if height[i - 1] <= height[i] and height[i] >= height[i + 1]:
                peaks.append((i, height[i]))

        npeaks = -1
        while npeaks != len(peaks):
            i = 1
            npeaks = len(peaks)
            while i < len(peaks) - 1:
                if peaks[i - 1][1] >= peaks[i][1] and peaks[i][1] <= peaks[i + 1][1]:
                    del peaks[i]
                else:
                    i += 1

        intervals = {}
        for i, ((l, lpeak), (r, rpeak)) in enumerate(zip(peaks, peaks[1:])):
            minpeak = min(lpeak, rpeak)
            intervals[l, r] = minpeak

        cnt = 0
        for (l, r), h in intervals.items():
            for i in range(l, r):
                diff = max(0, h - height[i])
                cnt += diff

        return cnt

