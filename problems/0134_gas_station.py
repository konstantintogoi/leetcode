"""
Solution of the medium problem
https://leetcode.com/problems/gas-station/
"Gas Station"
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Return the starting gas station's index.

        >>> Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        3
        >>> Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3])
        -1
        >>> Solution().canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6])
        3

        """
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            if tank < 0:
                tank = 0
                start = i + 1

        tank = 0
        for i in range(start, start + len(gas)):
            tank += (gas[i % len(gas)] - cost[i % len(gas)])
            if tank < 0:
                return -1

        return start

