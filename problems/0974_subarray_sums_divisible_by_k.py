"""
Solution of the medium problem
https://leetcode.com/problems/subarray-sums-divisible-by-k/
"Subarray Sums Divisible by K"
"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """Return the number of subarrays that have a sum divisible by `k`.

        >>> Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
        7
        >>> Solution().subarraysDivByK([5], 9)
        0

        """
        counter = defaultdict(int)
        counter[0] = 1

        res = 0
        cumsum = 0
        for num in nums:
            cumsum += num
            remainder = cumsum % k
            res += counter[remainder]
            counter[remainder] += 1

        return res

