"""
Solution of the easy problem
https://leetcode.com/problems/count-elements-with-maximum-frequency/
"Count Elements With Maximum Frequency"
"""
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """Return the total frequencies of elements in `nums`,
        s.t. those elements all have the maximum frequency.

        >>> Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4])
        4
        >>> Solution().maxFrequencyElements([1, 2, 3, 4, 5])
        5
        >>> Solution().maxFrequencyElements([15])
        1

        """
        maxcnt = 0
        freqs = {}
        freqnums = set()

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
            if freqs[num] > maxcnt:
                freqnums = {num}
                maxcnt = freqs[num]
            elif freqs[num] == maxcnt:
                freqnums.add(num)

        return maxcnt * len(freqnums)

