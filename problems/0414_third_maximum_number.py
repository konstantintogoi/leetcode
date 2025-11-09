"""
Solution of the easy problem
https://leetcode.com/problems/third-maximum-number/
"Third Maxium Number"
"""
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Return the third distinct maximum number in the `nums`.

        >>> Solution().thirdMax([3, 2, 1])
        1
        >>> Solution().thirdMax([1, 2])
        2
        >>> Solution().thirdMax([2, 2, 3, 1])
        1
        >>> Solution().thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3])
        0

        """
        m1 = None
        m2 = None
        m3 = None

        for num in nums:
            if m1 is None or num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num == m1:
                continue
            elif m2 is None or num > m2:
                m3 = m2
                m2 = num
            elif num == m2:
                continue
            elif m3 is None or num > m3:
                m3 = num

        return m1 if m3 is None else m3

