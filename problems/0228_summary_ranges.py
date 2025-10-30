"""
Solution of the easy problem
https://leetcode.com/problems/summary-ranges/
"Summary Ranges"
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """Return the smallest sorted list of ranges that cover all the nums.

        >>> Solution().summaryRanges([0, 1, 2, 4, 5, 7])
        ['0->2', '4->5', '7']
        >>> Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])
        ['0', '2->4', '6', '8->9']
        >>> Solution().summaryRanges([])
        []

        """
        intervals = []
        interval = []

        for num in nums:
            if interval and num == interval[-1] + 1:
                interval[-1] = num
            else:
                if interval: intervals.append(interval)
                interval = [num, num]

        if interval:
            intervals.append(interval)

        for i in range(len(intervals)):
            if intervals[i][0] == intervals[i][1]:
                intervals[i] = str(intervals[i][0])
            else:
                intervals[i] = f'{intervals[i][0]}->{intervals[i][1]}'

        return intervals

